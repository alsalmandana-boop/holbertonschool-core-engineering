#!/usr/bin/env python3
"""WebSocket server implementing unicast communication."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """Track clients and respond only to the sender."""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await websocket.send("U:" + message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket unicast server."""
    async with websockets.serve(
        connection_handler, "127.0.0.1", 8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

