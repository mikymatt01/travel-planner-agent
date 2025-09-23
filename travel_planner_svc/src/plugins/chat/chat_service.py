from src.agents.chatbot.listener.crew_listener import CrewListener
from src.agents.chatbot.chatbot import TravelSupportCrew
from utils.socket_sender import WebsocketSender, Type
from fastapi import WebSocket

async def progress_ws(websocket: WebSocket):
    CrewListener(websocket=websocket)
    while True:
        msg = await websocket.receive_json()
        prompt = msg.get('prompt')
        inputs = { "user_prompt": prompt }
        await WebsocketSender.send(websocket, "Thinking about the answer...", type=Type.LOG)
        result = await TravelSupportCrew().crew().kickoff_async(inputs=inputs)
        await WebsocketSender.send(websocket, str(result))
