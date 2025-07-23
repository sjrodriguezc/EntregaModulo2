from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Booking(BaseModel):
    id: int
    user_id: int
    room_id: int
    start_date: str
    end_date: str
    status: str

bookings: List[Booking] = []

@router.post("/bookings/", response_model=Booking)
def create_booking(booking: Booking):
    bookings.append(booking)
    return booking

@router.get("/bookings/", response_model=List[Booking])
def get_bookings():
    return bookings

@router.get("/bookings/{booking_id}", response_model=Booking)
def get_booking(booking_id: int):
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise HTTPException(status_code=404, detail="Booking not found")

@router.put("/bookings/{booking_id}", response_model=Booking)
def update_booking(booking_id: int, updated_booking: Booking):
    for index, booking in enumerate(bookings):
        if booking.id == booking_id:
            bookings[index] = updated_booking
            return updated_booking
    raise HTTPException(status_code=404, detail="Booking not found")

@router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int):
    for index, booking in enumerate(bookings):
        if booking.id == booking_id:
            bookings.pop(index)
            return {"message": "Booking deleted successfully"}
    raise HTTPException(status_code=404, detail="Booking not found")