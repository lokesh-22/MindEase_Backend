import uuid
from sqlalchemy.orm import Session

from app.db import models
from app.schemas.completed_activity import CompletedActivityCreate


def mark_completed(
    db: Session, user_id: str, completed_in: CompletedActivityCreate
) -> models.CompletedActivity:
    completed = models.CompletedActivity(
        id=str(uuid.uuid4()),
        user_id=user_id,
        activity_id=completed_in.activity_id,
        rating=completed_in.rating,
        note=completed_in.note,
    )
    db.add(completed)
    db.commit()
    db.refresh(completed)
    return completed


def list_completed(db: Session, user_id: str):
    return db.query(models.CompletedActivity).filter(models.CompletedActivity.user_id == user_id).all()
