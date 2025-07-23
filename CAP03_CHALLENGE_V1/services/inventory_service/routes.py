from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
rooms_db = {}

class Room(BaseModel):
    name: str
    type: str
    price: float
    availability: bool

@router.get("/rooms")
def get_rooms():
    return list(rooms_db.values())

@router.post("/rooms", status_code=201)
def create_room(room: Room):
    room_id = len(rooms_db) + 1
    room_data = room.model_dump()
    room_data["id"] = room_id
    rooms_db[room_id] = room_data
    return room_data

@router.put("/rooms/{room_id}")
def update_room(room_id: int, room: Room):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="Room not found")
    room_data = room.model_dump()
    room_data["id"] = room_id
    rooms_db[room_id] = room_data
    return room_data

@router.delete("/rooms/{room_id}", status_code=204)
def delete_room(room_id: int):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="Room not found")
    del rooms_db[room_id]
    return

@router.get("/rooms/{room_id}")
def get_room(room_id: int):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="Room not found")
    return rooms_db[room_id]