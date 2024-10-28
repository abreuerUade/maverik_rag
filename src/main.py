from fastapi import FastAPI
from .routers import chat
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Maverik",
    description="Asistente financiero basado en la filosofía de Warren Buffett",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir orígenes específicos si es necesario
    allow_credentials=True,
    allow_methods=["*"],  # Incluye GET para /openapi.json
    allow_headers=["*"],  # Permite todos los headers
)


app.get("/")(lambda: {"message": "Bienvenido a Maverik"})

app.include_router(chat.router)
handler = Mangum(app)
