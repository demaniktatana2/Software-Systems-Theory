from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

STUDENT_N = 5
app = FastAPI(title=f"Payment Service N{STUDENT_N}")

BILLING_SERVICE_URL = "http://billing-service-05:8000"

class PaymentRequest(BaseModel):
    bill_id: int
    amount: float

@app.post("/payments")
def process_payment(payment: PaymentRequest):
    try:
        response = requests.get(f"{BILLING_SERVICE_URL}/bills/{payment.bill_id}")
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Billing Service unavailable")

    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="Bill does not exist")
    
    bill_info = response.json()["bill_data"]
    
    if payment.amount < bill_info["amount"]:
        raise HTTPException(status_code=400, detail="Insufficient amount provided")

    return {
        "student_id": STUDENT_N,
        "status": "Success",
        "bill_id": payment.bill_id,
        "processed_amount": payment.amount
    }