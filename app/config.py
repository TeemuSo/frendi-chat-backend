import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    
    # Base
    APP_NAME: str = "Frendi Chat API"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "API for Frendi Chat Backend"
    
    # Server
    PORT: int = int(os.getenv("PORT", 8000))
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = ENV == "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create a singleton instance
settings = Settings() 