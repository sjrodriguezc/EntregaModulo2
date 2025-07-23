from fastapi import APIRouter
import httpx

router = APIRouter()

AUTH_SERVICE_URL = "http://auth_service"
BOOKING_SERVICE_URL = "http://booking_service"
INVENTORY_SERVICE_URL = "http://inventory_service"
PAYMENT_SERVICE_URL = "http://payment_service"
NOTIFICATION_SERVICE_URL = "http://notification_service"
USER_PROFILE_SERVICE_URL = "http://user_profile_service"

@router.post("/auth/register")
async def register_user(user_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/register", json=user_data)
    return response.json()

@router.post("/auth/login")
async def login_user(credentials: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/login", json=credentials)
    return response.json()

@router.post("/booking")
async def create_booking(booking_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BOOKING_SERVICE_URL}/book", json=booking_data)
    return response.json()

@router.put("/booking/{booking_id}")
async def update_booking(booking_id: str, booking_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BOOKING_SERVICE_URL}/book/{booking_id}", json=booking_data)
    return response.json()

@router.delete("/booking/{booking_id}")
async def cancel_booking(booking_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BOOKING_SERVICE_URL}/book/{booking_id}")
    return response.json()

@router.get("/inventory")
async def get_inventory():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{INVENTORY_SERVICE_URL}/rooms")
    return response.json()

@router.post("/payment")
async def process_payment(payment_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{PAYMENT_SERVICE_URL}/pay", json=payment_data)
    return response.json()

@router.post("/notifications/send")
async def send_notification(notification_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{NOTIFICATION_SERVICE_URL}/send", json=notification_data)
    return response.json()

@router.get("/user/{user_id}")
async def get_user_profile(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_PROFILE_SERVICE_URL}/profile/{user_id}")
    return response.json()