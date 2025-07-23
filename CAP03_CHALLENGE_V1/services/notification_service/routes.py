from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class NotificationRequest(BaseModel):
    recipient: str
    message: str

@router.post("/send_email")
async def send_email(notification: NotificationRequest):
    # Aquí se implementaría la lógica para enviar un correo electrónico
    return {"status": "success", "message": f"Email sent to {notification.recipient}"}

@router.post("/send_sms")
async def send_sms(notification: NotificationRequest):
    # Aquí se implementaría la lógica para enviar un mensaje SMS
    return {"status": "success", "message": f"SMS sent to {notification.recipient}"}