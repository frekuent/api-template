import django
import pytest
from fastapi.testclient import TestClient

from app.main import app

django.setup()

client = TestClient(app)


@pytest.mark.django_db
def test_create_item():
    item_data = {"name": "Test Item", "description": "A test item", "price": 9.99}
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]


@pytest.mark.django_db
def test_get_item():
    item_data = {"name": "Test Item", "description": "A test item", "price": 9.99}
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    item_id = response.json()["id"]

    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]


@pytest.mark.django_db
def test_get_nonexistent_item():
    response = client.get("/api/v1/items/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
