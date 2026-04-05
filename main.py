from_attributes = True
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance API 🚀")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Finance API running"}

@app.post("/transactions")
def create(txn: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, txn)

@app.get("/transactions")
def read(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.delete("/transactions/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    crud.delete_transaction(db, id)
    return {"message": "Deleted"}

@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    txns = crud.get_transactions(db)

    income = sum(t.amount for t in txns if t.type == "income")
    expense = sum(t.amount for t in txns if t.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }