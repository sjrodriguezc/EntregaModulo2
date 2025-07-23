# tests/payment_service/test_payment_service.py

import pytest
from fastapi.testclient import TestClient
from services.payment_service.app import app

client = TestClient(app)

def test_create_payment():
    response = client.post("/payments/", json={"amount": 100, "method": "credit_card"})
    assert response.status_code == 201
    assert response.json() == {"status": "success", "transaction_id": "12345"}

def test_create_payment_invalid_amount():
    response = client.post("/payments/", json={"amount": -100, "method": "credit_card"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid amount"}

def test_verify_payment():
    response = client.get("/payments/verify/12345")
    assert response.status_code == 200
    assert response.json() == {"status": "verified", "transaction_id": "12345"}

def test_verify_payment_not_found():
    response = client.get("/payments/verify/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Transaction not found"}