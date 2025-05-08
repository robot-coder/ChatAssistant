from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post('/api/chat')
async def chat(message: Message):
    # Here you would integrate LiteLLM to get a response
    # For now, we'll just echo the message back
    response = f'You said: {message.message}'
    return {'response': response}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)