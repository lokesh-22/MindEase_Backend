import uuid
from sqlalchemy.orm import Session

from app.db import models
from app.schemas.journal import JournalCreate


def create_entry(db: Session, user_id: str, journal_in: JournalCreate) -> models.JournalEntry:
    entry = models.JournalEntry(
        id=str(uuid.uuid4()),
        user_id=user_id,
        title=journal_in.title,
        content=journal_in.content,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def list_entries(db: Session, user_id: str):
    return db.query(models.JournalEntry).filter(models.JournalEntry.user_id == user_id).all()
