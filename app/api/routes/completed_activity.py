from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db_session
from app.schemas.completed_activity import (
    CompletedActivityCreate,
    CompletedActivityRead,
)
from app.services import completed_activity_service

router = APIRouter(prefix="/completed", tags=["completed_activities"])


@router.post("/", response_model=CompletedActivityRead)
def mark_completed(
    completed_in: CompletedActivityCreate,
    db: Session = Depends(get_db_session),
    current_user=Depends(get_current_user),
):
    return completed_activity_service.mark_completed(db, current_user.id, completed_in)


@router.get("/", response_model=list[CompletedActivityRead])
def list_completed(
    db: Session = Depends(get_db_session), current_user=Depends(get_current_user)
):
    return completed_activity_service.list_completed(db, current_user.id)
