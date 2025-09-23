from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import crewai
import os

from src.plugins.chat import chat_controller

print(crewai.__version__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_controller.router)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)