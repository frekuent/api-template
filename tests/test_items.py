import pytest
from fastapi.testclient import TestClient

from app.main import app

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
    assert data["is_available"] is True


@pytest.mark.django_db
def test_get_item():
    item_data = {"name": "Test Item", "description": "A test item", "price": 9.99}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]

    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]


@pytest.mark.django_db
def test_update_item():
    item_data = {"name": "Test Item", "description": "A test item", "price": 9.99}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]

    updated_data = {"name": "Updated Item", "description": "An updated item", "price": 19.99}
    update_response = client.put(f"/api/v1/items/{item_id}", json=updated_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["id"] == item_id
    assert data["name"] == updated_data["name"]
    assert data["description"] == updated_data["description"]
    assert data["price"] == updated_data["price"]


@pytest.mark.django_db
def test_delete_item():
    item_data = {"name": "Test Item", "description": "A test item", "price": 9.99}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]

    delete_response = client.delete(f"/api/v1/items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"detail": "Item deleted"}

    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Item not found"}
