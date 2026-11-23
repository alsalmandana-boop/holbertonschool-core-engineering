# Real-time Communication with WebSockets

## Description

This project is part of the Holberton School Core Engineering curriculum.

The goal is to understand real-time communication using WebSockets and asynchronous programming in Python.

Unlike traditional HTTP communication, WebSockets allow clients and servers to maintain a persistent connection and exchange messages in both directions.

## Learning Objectives

- Understand how WebSockets work.
- Learn the difference between HTTP and WebSocket communication.
- Create a WebSocket server using Python.
- Use asynchronous programming with `async` and `await`.
- Handle multiple client connections.
- Send and receive messages in real time.
- Keep connections open for continuous communication.

## Technologies Used

- Python 3
- WebSockets library
- asyncio

## Task 0: WebSocket Echo Server

The objective of this task is to create a WebSocket server that receives text messages from clients and sends back the exact same messages.

The server listens on `127.0.0.1` at port `8765`.

### File

`echo_server.py` — Implements the WebSocket echo server.

### How It Works

1. The client connects to the WebSocket server.
2. The server accepts the connection.
3. The client sends a text message.
4. The server sends back the same message without modification.
5. The connection remains open for additional messages.

## Installation

Install the required Python library:

```bash
python3 -m pip install websockets
```

## Usage

Start the server:

```bash
python3 echo_server.py
```

Open another terminal and connect using the WebSockets interactive client:

```bash
websockets ws://127.0.0.1:8765/
```

### Example

```text
Connected to ws://127.0.0.1:8765/
> Hello
< Hello
> How are you?
< How are you?
```

## Key Concepts

**WebSocket:** A communication protocol that allows continuous, bidirectional communication between a client and a server.

**Asynchronous Programming:** A programming approach that allows multiple operations to be handled without blocking each other while waiting.

**async/await:** Python keywords used to define and manage asynchronous operations.

**Echo Server:** A server that sends received messages back to the sender without modifying them.

## Requirements

- Python 3
- PEP 8 coding style
- Python files must start with `#!/usr/bin/env python3`
- All Python files must end with a newline.

## Author

Dana Ibrahim Alsalman

Holberton School trainee
