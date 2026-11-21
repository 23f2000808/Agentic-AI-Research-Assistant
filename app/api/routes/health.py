"""Health check endpoint router."""

from fastapi import APIRouter
from app.config import get_settings

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return health status of the application service."""
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
    }
