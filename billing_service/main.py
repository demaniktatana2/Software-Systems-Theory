from fastapi import FastAPI, HTTPException

STUDENT_N = 5
app = FastAPI(title=f"Billing Service N{STUDENT_N}")

BILLS = {
    501: {"id": 501, "type": "Електроенергія", "amount": 450.50, "status": "unpaid"},
    502: {"id": 502, "type": "Водопостачання", "amount": 210.00, "status": "unpaid"}
}

@app.get("/bills/{bill_id}")
def get_bill(bill_id: int):
    if bill_id not in BILLS:
        raise HTTPException(status_code=404, detail="Рахунок не знайдено")
    return {"student_id": STUDENT_N, "bill_data": BILLS[bill_id]}