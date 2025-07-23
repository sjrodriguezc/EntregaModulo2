from pydantic import BaseModel
from typing import List, Optional

class Notification(BaseModel):
    id: int
    recipient: str
    message: str
    status: str  # e.g., "pending", "sent", "failed"
    created_at: str  # ISO format date string
    updated_at: str  # ISO format date string

class EmailNotification(Notification):
    subject: str

class SMSNotification(Notification):
    phone_number: str

class NotificationResponse(BaseModel):
    success: bool
    message: str
    notification: Optional[Notification] = None

class NotificationListResponse(BaseModel):
    notifications: List[Notification]