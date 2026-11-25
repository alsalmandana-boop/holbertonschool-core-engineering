#!/usr/bin/env python3
"""A simple WebSocket client."""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send one message and return the server response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
     


async def main():
    """Connect to the echo server and print its response."""
    response = await connect_and_send(
        "ws://localhost:8765", "Hello WebSocket"
    )
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())

