from sqlalchemy.orm import Session
import models

def create_transaction(db: Session, txn):
    new_txn = models.Transaction(**txn.dict())
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return new_txn

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def delete_transaction(db: Session, txn_id: int):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()
    db.delete(txn)
    db.commit()