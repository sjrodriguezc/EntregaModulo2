from fastapi.testclient import TestClient
from api_gateway.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Bienvenido al API Gateway del Sistema de Reservas de Habitaciones!"}

