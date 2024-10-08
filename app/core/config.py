from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    TAVILY_API_KEY: str
    MONGODB_ATLAS_CLUSTER_URI: str
    DB_NAME: str = "langchain_db"
    COLLECTION_NAME: str = "langchain_vectorstores"
    ATLAS_VECTOR_SEARCH_INDEX_NAME: str = "vector_index"

    class Config:
        env_file = ".env"


settings = Settings()
