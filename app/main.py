from fastapi import FastAPI
from app.routers import chat
from app.core.config import settings

app = FastAPI(
    title="Maverik",
    description="Asistente financiero basado en la filosofía de Warren Buffett",
    version="1.0.0",
)

app.get("/")(lambda: {"message": "Bienvenido a Maverik"})

app.include_router(chat.router)
