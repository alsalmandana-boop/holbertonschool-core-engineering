
#!/usr/bin/env python3
"""ASGI application with HTTP and WebSocket support."""

from pathlib import Path
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    """Return the original HTML homepage."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def chat_page(request):
    """Return the browser chat interface."""
    return FileResponse(BASE_DIR / "index.html")


async def stylesheet(request):
    """Return the CSS stylesheet."""
    return FileResponse(BASE_DIR / "styles.css")


async def javascript(request):
    """Return the JavaScript file."""
    return FileResponse(BASE_DIR / "chat.js")


async def websocket_endpoint(websocket):
    """Receive and echo WebSocket messages."""
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    Route("/chat", chat_page),
    Route("/styles.css", stylesheet),
    Route("/chat.js", javascript),
    WebSocketRoute("/ws", websocket_endpoint),
])
