import fastapi
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello, this is the Chat Assistant!</h1>"

# Add more endpoints for chat functionality
