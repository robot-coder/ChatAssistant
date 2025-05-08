from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return open("app/index.html").read()

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    messages = []  # Store conversation messages
    while True:
        data = await websocket.receive_text()
        messages.append(data)  # Add user message to conversation
        # Here you would call the LLM and get a response
        response = "This is a response from the LLM"  # Placeholder response
        messages.append(response)  # Add LLM response to conversation
        await websocket.send_text(json.dumps(messages))
