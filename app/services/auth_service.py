import uuid

from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash, verify_password
from app.db import models
from app.schemas.user import Token, UserCreate


def register_user(db: Session, user_in: UserCreate) -> Token:
    hashed_password = get_password_hash(user_in.password)
    user = models.User(
        id=str(uuid.uuid4()),
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed_password,
        anonymous_id=str(uuid.uuid4()),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(subject=user.id)
    return Token(access_token=token)


def authenticate(db: Session, email: str, password: str) -> Token | None:
    user = (
        db.query(models.User)
        .filter(models.User.email == email)
        .first()
    )
    if not user or not verify_password(password, user.hashed_password):
        return None
    token = create_access_token(subject=user.id)
    return Token(access_token=token)
