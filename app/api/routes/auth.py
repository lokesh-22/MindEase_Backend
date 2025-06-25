from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.schemas.user import Token, UserCreate, UserLogin
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db_session)):
    return auth_service.register_user(db, user_in)


@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db_session)):
    token = auth_service.authenticate(db, credentials.email, credentials.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return token
