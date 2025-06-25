from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db_session
from app.schemas.journal import JournalCreate, JournalRead
from app.services import journal_service

router = APIRouter(prefix="/journals", tags=["journals"])


@router.post("/", response_model=JournalRead)
def create_entry(
    journal_in: JournalCreate,
    db: Session = Depends(get_db_session),
    current_user=Depends(get_current_user),
):
    return journal_service.create_entry(db, current_user.id, journal_in)


@router.get("/", response_model=list[JournalRead])
def list_entries(
    db: Session = Depends(get_db_session), current_user=Depends(get_current_user)
):
    return journal_service.list_entries(db, current_user.id)
