from fastapi import FastAPI
from app.routers import chat

app = FastAPI(
    title="Maverik Financial Assistant",
    description="Asistente financiero basado en la filosofía de Warren Buffett",
    version="1.0.0",
)

app.include_router(chat.router)
