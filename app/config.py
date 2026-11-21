"""Application configuration using Pydantic Settings."""

from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # API Keys & LLM settings
    google_api_key: Optional[str] = None
    model_name: str = "gemini-2.5-flash"

    # Application settings
    app_name: str = "agentic-research-assistant"
    debug: bool = False


@lru_cache()
def get_settings() -> Settings:
    """Return cached application settings instance."""
    return Settings()
