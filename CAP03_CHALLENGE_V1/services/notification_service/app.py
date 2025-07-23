from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Notification(BaseModel):
    recipient: str
    message: str

notifications = []

@app.post("/notifications/", response_model=Notification)
def send_notification(notification: Notification):
    notifications.append(notification)
    return notification

@app.get("/notifications/", response_model=List[Notification])
def get_notifications():
    return notifications

@app.delete("/notifications/{recipient}", response_model=Notification)
def delete_notification(recipient: str):
    for notification in notifications:
        if notification.recipient == recipient:
            notifications.remove(notification)
            return notification
    raise HTTPException(status_code=404, detail="Notification not found")