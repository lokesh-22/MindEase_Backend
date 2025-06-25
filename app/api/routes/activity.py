from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db_session
from app.schemas.activity import ActivitySuggestionCreate, ActivitySuggestionRead
from app.services import activity_service

router = APIRouter(prefix="/activities", tags=["activities"])


@router.post("/", response_model=ActivitySuggestionRead)
def create_suggestion(
    activity_in: ActivitySuggestionCreate,
    db: Session = Depends(get_db_session),
    _=Depends(get_current_user),  # Only authenticated users can add
):
    return activity_service.create_suggestion(db, activity_in)


@router.get("/", response_model=list[ActivitySuggestionRead])
def list_suggestions(db: Session = Depends(get_db_session)):
    return activity_service.list_suggestions(db)
