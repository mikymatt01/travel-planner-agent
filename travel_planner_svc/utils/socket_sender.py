class Type:
    LOG = "log"
    MESSAGE = "message"
    
class WebsocketSender():
    async def send(websocket, message, type=None):
        if type:
            await websocket.send_json({"message": message, "type": type})
        else:
            await websocket.send_json({"message": message})