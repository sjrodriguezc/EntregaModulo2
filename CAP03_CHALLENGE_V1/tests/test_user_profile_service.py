# tests/user_profile_service/test_user_profile_service.py

import pytest
from fastapi.testclient import TestClient
from services.user_profile_service.app import app

client = TestClient(app)

def test_create_user_profile():
    response = client.post("/user_profiles/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

def test_get_user_profile():
    response = client.get("/user_profiles/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

def test_update_user_profile():
    response = client.put("/user_profiles/1", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Doe", "email": "jane@example.com"}

def test_delete_user_profile():
    response = client.delete("/user_profiles/1")
    assert response.status_code == 204

def test_get_nonexistent_user_profile():
    response = client.get("/user_profiles/999")
    assert response.status_code == 404