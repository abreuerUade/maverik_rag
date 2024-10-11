from fastapi import FastAPI
from .routers import chat
from mangum import Mangum


app = FastAPI(
    title="Maverik",
    description="Asistente financiero basado en la filosofía de Warren Buffett",
    version="1.0.0",
    root_path="/api"
)

app.get("/ping")(lambda: {"message": "Bienvenido a Maverik"})

app.include_router(chat.router)

handler = Mangum(app)
