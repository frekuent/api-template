from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_status_check():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}
