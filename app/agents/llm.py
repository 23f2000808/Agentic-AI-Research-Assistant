"""LLM connection abstraction using LangChain and Google Gemini."""

from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import get_settings


def get_llm(
    model_name: str | None = None,
    temperature: float = 0.0,
) -> ChatGoogleGenerativeAI:
    """Create and return a configured ChatGoogleGenerativeAI instance.

    Args:
        model_name: Optional override for the model name. Defaults to settings.model_name.
        temperature: Sampling temperature for generation (0.0 for deterministic output).

    Returns:
        ChatGoogleGenerativeAI: Configured LangChain chat model.

    Raises:
        ValueError: If GOOGLE_API_KEY is not set in configuration.
    """
    settings = get_settings()

    if not settings.google_api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not configured. Please set it in your .env file."
        )

    return ChatGoogleGenerativeAI(
        model=model_name or settings.model_name,
        google_api_key=settings.google_api_key,
        temperature=temperature,
    )
