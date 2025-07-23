# tests/inventory_service/test_inventory_service.py

from fastapi.testclient import TestClient
from services.inventory_service.app import app

client = TestClient(app)

def test_get_rooms():
    response = client.get("/rooms")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_room():
    room_data = {
        "name": "Room 101",
        "type": "single",
        "price": 100.0,
        "availability": True
    }
    response = client.post("/rooms", json=room_data)
    assert response.status_code == 201
    assert response.json()["name"] == room_data["name"]

def test_update_room():
    room_data = {
        "name": "Room 101",
        "type": "single",
        "price": 120.0,
        "availability": True
    }
    response = client.put("/rooms/1", json=room_data)
    assert response.status_code == 200
    assert response.json()["price"] == room_data["price"]

def test_delete_room():
    response = client.delete("/rooms/1")
    assert response.status_code == 204

def test_get_room_not_found():
    response = client.get("/rooms/999")
    assert response.status_code == 404