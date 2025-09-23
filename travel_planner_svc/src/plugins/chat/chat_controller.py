from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.plugins.chat import chat_service

router = APIRouter()

@router.websocket("/ws/chat")
async def progress_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        chat_service.progress_ws(websocket)
    except WebSocketDisconnect:
        print(f"WebSocket disconnected")
