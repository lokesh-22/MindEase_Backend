from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db_session
from app.schemas.mood import MoodCreate, MoodRead
from app.services import mood_service

router = APIRouter(prefix="/moods", tags=["moods"])


@router.post("/", response_model=MoodRead)
def create_mood(
    mood_in: MoodCreate,
    db: Session = Depends(get_db_session),
    current_user=Depends(get_current_user),
):
    return mood_service.create_mood(db, current_user.id, mood_in)


@router.get("/", response_model=list[MoodRead])
def list_moods(
    db: Session = Depends(get_db_session), current_user=Depends(get_current_user)
):
    return mood_service.list_moods(db, current_user.id)
