from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    messages: list
    llm: str

@app.post('/api/chat')
async def chat(message: Message):
    # Here you would call your LLM API using LiteLLM
    # For demonstration, we will return a mock response
    response = f'You said: {message.messages[-1]['content']}'
    return {'response': response}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)