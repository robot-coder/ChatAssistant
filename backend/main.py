from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Message(BaseModel):
    messages: list

@app.post('/api/chat')
async def chat(message: Message):
    # Here you would integrate LiteLLM to get a response
    response = "This is a placeholder response."
    return {'response': response}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)