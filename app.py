import uvicorn
from chatbot import ChatBot, Chat
from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect
)

app = FastAPI()

chatbot = ChatBot()


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WS connect.")

    try:
        chat = Chat(chatbot=chatbot)

        while True:
            data = await websocket.receive_text()
            bot_reply = await chat.get_reply(data)
            await websocket.send_text(bot_reply)
    except WebSocketDisconnect:
        print("WS was closed.")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

