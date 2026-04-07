from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

app = FastAPI()
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = AsyncOpenAI(api_key=api_key)

@app.get('/health')
def health():
    return {"status": "ok"}

class UserMessage(BaseModel):
    message: str
    chat_id: int

@app.post('/chat')
async def chat(user_text: UserMessage):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Отвечай спокойно, без лишней воды"},
            {"role": "user", "content": user_text.message}
        ]
    )
    return response.choices[0].message.content