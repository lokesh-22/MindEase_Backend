from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.db import models
from app.db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db_session():
    yield from get_db()


def get_current_user(
    db: Session = Depends(get_db_session), token: str = Depends(oauth2_scheme)
):
    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
