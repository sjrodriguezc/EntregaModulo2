from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
payments_db = {}

class PaymentRequest(BaseModel):
    amount: float
    method: str

@router.post("/payments/", status_code=201)
def create_payment(payment: PaymentRequest):
    if payment.amount < 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    transaction_id = "12345"
    payments_db[transaction_id] = {"status": "success", "transaction_id": transaction_id}
    return {"status": "success", "transaction_id": transaction_id}

@router.get("/payments/verify/{transaction_id}")
def verify_payment(transaction_id: str):
    if transaction_id not in payments_db:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"status": "verified", "transaction_id": transaction_id}