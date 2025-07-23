import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from services.booking_service.app import app  # Ajusta el import si mueves el archivo booking_service.py

client = TestClient(app)

def test_create_booking():
    booking_data = {
        "id": 1,
        "user_id": 101,
        "room_id": 202,
        "start_date": "2025-07-20",
        "end_date": "2025-07-21",
        "status": "confirmed"
    }
    response = client.post("/bookings/", json=booking_data)
    assert response.status_code == 200
    assert response.json() == booking_data

def test_get_bookings():
    response = client.get("/bookings/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_booking():
    response = client.get("/bookings/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_booking():
    updated_data = {
        "id": 1,
        "user_id": 101,
        "room_id": 202,
        "start_date": "2025-07-22",
        "end_date": "2025-07-23",
        "status": "cancelled"
    }
    response = client.put("/bookings/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["status"] == "cancelled"

def test_delete_booking():
    response = client.delete("/bookings/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Booking deleted successfully"}

def test_get_nonexistent_booking():
    response = client.get("/bookings/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Booking not found"