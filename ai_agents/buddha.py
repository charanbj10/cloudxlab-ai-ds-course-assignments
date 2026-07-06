from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from buddha_agent import BuddhaAgent

app = FastAPI()

agent = BuddhaAgent()

app.mount("/static", StaticFiles(directory="static"), name="static")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat(req: ChatRequest):

    reply = agent.chat(req.message)

    return {
        "reply": reply
    }



# run cmd : uvicorn buddha:app --reload