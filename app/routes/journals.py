from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from .dependencies import get_db, get_current_user
from typing import List

router = APIRouter(prefix="/journal", tags=["journal"])

@router.post("/", response_model=schemas.JournalEntryOut)
def create_entry(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_entry = models.JournalEntry(**entry.dict(), user_id=current_user.id)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/", response_model=List[schemas.JournalEntryOut])
def get_entries(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.JournalEntry).filter(models.JournalEntry.user_id == current_user.id).all()
