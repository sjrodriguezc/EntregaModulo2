from fastapi import FastAPI
from services.inventory_service.routes import router as inventory_router
app = FastAPI()

app.include_router(inventory_router)

@app.get("/rooms")
async def get_rooms():
    return {"message": "List of available rooms"}

@app.post("/rooms")
async def add_room(room: dict):
    return {"message": "Room added", "room": room}

@app.put("/rooms/{room_id}")
async def update_room(room_id: int, room: dict):
    return {"message": "Room updated", "room_id": room_id, "room": room}

@app.delete("/rooms/{room_id}")
async def delete_room(room_id: int):
    return {"message": "Room deleted", "room_id": room_id}