# tests/auth_service/test_auth_service.py


from services.auth_service.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert response.json() == {"message": "User created successfully"}

def test_login_user():
    client.post("/register", json={"username": "testuser", "password": "testpass"})
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_user_invalid_credentials():
    response = client.post("/login", json={"username": "invaliduser", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}

def test_get_current_user():
    client.post("/register", json={"username": "testuser", "password": "testpass"})
    login_response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    access_token = login_response.json()["access_token"]
    response = client.get("/users/me", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json() == {"username": "testuser"}