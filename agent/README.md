# FastAPI Message Receiver

A simple FastAPI server that receives POST messages and prints them to the console.

## Features

- **POST /message** - Receive and print messages
- **GET /messages** - View all received messages
- **GET /** - API information and available endpoints

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using pip with pyproject.toml:
```bash
pip install -e .
```

## Usage

### Start the server

```bash
python main.py
```

The server will start on `http://localhost:8000`

### API Endpoints

#### POST /message
Send a message to be printed:

```bash
curl -X POST "http://localhost:8000/message" \
     -H "Content-Type: application/json" \
     -d '{"content": "Hello, World!", "sender": "user123"}'
```

#### GET /messages
Retrieve all received messages:

```bash
curl "http://localhost:8000/messages"
```

#### GET /
Get API information:

```bash
curl "http://localhost:8000/"
```

### Test the API

Run the test script to see the API in action:

```bash
python test_api.py
```

## Message Format

Messages should be sent as JSON with the following structure:

```json
{
    "content": "Your message here",
    "sender": "username"  // Optional, defaults to "anonymous"
}
```

## Interactive API Documentation

Once the server is running, you can view the interactive API documentation at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Example Response

When you send a message, you'll get a response like:

```json
{
    "status": "success",
    "message": "Message received and printed",
    "received": {
        "sender": "user123",
        "content": "Hello, World!"
    }
}
```

The message will also be printed to the server console.
