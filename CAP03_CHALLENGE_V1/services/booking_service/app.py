from fastapi import FastAPI
from services.booking_service.routes import router as booking_router

app = FastAPI(title="Booking Service")

app.include_router(booking_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Booking Service"}