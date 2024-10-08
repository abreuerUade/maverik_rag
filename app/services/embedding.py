from langchain_openai import OpenAIEmbeddings
from app.core.config import settings
import os

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=1024
)
