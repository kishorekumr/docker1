import asyncio
import websockets
import time

class WebSocketServer:
    def __init__(self):
        self.start_time = None

    async def handle_connection(self, websocket, path):
        self.start_time = time.time()
        async for message in websocket:
            if message == "Ping":
                latency = (time.time() - self.start_time) * 1000  # Convert to milliseconds
                await websocket.send(f"Pong received: {latency:.2f} ms")
                self.start_time = time.time()  # Update start time

async def main():
    server = WebSocketServer()
    async with websockets.serve(server.handle_connection, "0.0.0.0", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
