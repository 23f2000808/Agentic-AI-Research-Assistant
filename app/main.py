"""Main entry point for the FastAPI application."""

from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title="Agentic AI Research Assistant",
    description="Backend API for the Agentic AI Research Assistant (Milestone v0.1)",
    version="0.1.0",
    debug=settings.debug,
)

# Register routers
app.include_router(health_router)


@app.get("/")
async def root() -> dict[str, str]:
    """Root welcome endpoint."""
    return {
        "message": f"Welcome to {settings.app_name} (v0.1)",
        "docs": "/docs",
        "health": "/health",
    }
