from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/send_notification")
def send_notification(email: str, message: str):
    # Simulate sending a notification
    return {"status": "success", "email": email, "message": message}

client = TestClient(app)

def test_send_notification():
    response = client.get("/send_notification?email=test@example.com&message=Hello")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "email": "test@example.com", "message": "Hello"}