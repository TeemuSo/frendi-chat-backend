from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    openai_api_key: str
    zep_api_key: str
    zep_api_url: str = "https://api.getzep.com"  # Default ZepAI API URL
    debug: bool = False
    port: int = 8000

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings() 