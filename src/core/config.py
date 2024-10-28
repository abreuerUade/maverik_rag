from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    OPENAI_API_KEY: str
    SERPAPI_API_KEY: str
    GOOGLE_CSE_ID: str
    GOOGLE_API_KEY: str
    FMP_API_KEY: str
    MONGODB_ATLAS_CLUSTER_URI: str
    DB_NAME: str = "langchain_db"
    COLLECTION_NAME: str = "langchain_vectorstores"
    ATLAS_VECTOR_SEARCH_INDEX_NAME: str = "vector_index"


settings = Settings()

