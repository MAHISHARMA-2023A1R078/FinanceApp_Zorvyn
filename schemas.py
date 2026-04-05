from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    notes: str

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True   # updated (no warning)