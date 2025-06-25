import uuid
from sqlalchemy.orm import Session

from app.db import models
from app.schemas.mood import MoodCreate


def create_mood(db: Session, user_id: str, mood_in: MoodCreate) -> models.MoodEntry:
    mood = models.MoodEntry(
        id=str(uuid.uuid4()),
        user_id=user_id,
        mood=mood_in.mood,
        note=mood_in.note,
    )
    db.add(mood)
    db.commit()
    db.refresh(mood)
    return mood


def list_moods(db: Session, user_id: str):
    return db.query(models.MoodEntry).filter(models.MoodEntry.user_id == user_id).all()
