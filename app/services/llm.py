import os
from langchain_openai import ChatOpenAI
from app.core.config import settings
from langchain_huggingface import HuggingFaceEndpoint


# Configuración de la clave API de OpenAI
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

# Modelo principal de OpenAI
model_ai = "gpt-3.5-turbo"
llm = ChatOpenAI(model_name=model_ai)

# Modelo de HuggingFace
hf_llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3.5-mini-instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)

hf_llm.bind(max_tokens=8000)



