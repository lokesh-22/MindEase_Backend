import uuid
from sqlalchemy.orm import Session

from app.db import models
from app.schemas.activity import ActivitySuggestionCreate


def create_suggestion(
    db: Session, activity_in: ActivitySuggestionCreate
) -> models.ActivitySuggestion:
    activity = models.ActivitySuggestion(
        id=str(uuid.uuid4()),
        title=activity_in.title,
        description=activity_in.description,
        category=activity_in.category,
        tags=activity_in.tags,
    )
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


def list_suggestions(db: Session):
    return db.query(models.ActivitySuggestion).all()
