from src.chatbot.listener.crew_listener import CrewListener
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from src.chatbot.chatbot import TravelSupportCrew
from utils.socket_sender import WebsocketSender, Type
import uvicorn
import crewai
import os

print(crewai.__version__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/chat")
async def progress_ws(websocket: WebSocket):
    await websocket.accept()
    CrewListener(websocket=websocket)
    try:
        while True:
            msg = await websocket.receive_json()
            prompt = msg.get('prompt')
            inputs = { "user_prompt": prompt }
            await WebsocketSender.send(websocket, "Thinking about the answer...", type=Type.LOG)
            result = await TravelSupportCrew().crew().kickoff_async(inputs=inputs)
            await WebsocketSender.send(websocket, str(result))
    except WebSocketDisconnect:
        print(f"WebSocket disconnected")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)