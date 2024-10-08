import os
from langchain_openai import ChatOpenAI
from app.core.config import settings


# Configuración de la clave API de OpenAI
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

# Modelo principal de OpenAI
model_ai = "gpt-3.5-turbo"
llm = ChatOpenAI(model_name=model_ai)
