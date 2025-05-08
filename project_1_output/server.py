import fastapi
from fastapi.responses import HTMLResponse
from fastapi import Request

app = fastapi.FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Welcome to the Chat Assistant</h1>"

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    # Here you would call your LLM and get a response
    llm_response = f"Response from LLM for: {user_message}"
    return {"response": llm_response}
