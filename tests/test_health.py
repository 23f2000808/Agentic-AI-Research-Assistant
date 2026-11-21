"""Unit test for the /health endpoint."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Fixture providing a TestClient instance for the FastAPI app."""
    return TestClient(app)


def test_health_check(client: TestClient) -> None:
    """Verify that GET /health returns 200 with expected service details."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "agentic-research-assistant"


def test_root_endpoint(client: TestClient) -> None:
    """Verify that GET / returns 200 and points to documentation and health."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["health"] == "/health"
