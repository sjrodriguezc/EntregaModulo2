from fastapi import FastAPI
from services.payment_service.routes import router as payment_router
app = FastAPI()

app.include_router(payment_router)

@app.post("/payments/")
async def create_payment(amount: float, method: str):
    return {"message": "Payment created", "amount": amount, "method": method}

@app.get("/payments/{payment_id}")
async def get_payment(payment_id: int):
    return {"message": "Payment details", "payment_id": payment_id}

@app.put("/payments/{payment_id}")
async def update_payment(payment_id: int, amount: float):
    return {"message": "Payment updated", "payment_id": payment_id, "amount": amount}

@app.delete("/payments/{payment_id}")
async def delete_payment(payment_id: int):
    return {"message": "Payment deleted", "payment_id": payment_id}