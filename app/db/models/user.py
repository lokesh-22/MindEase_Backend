from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    anonymous_id = Column(String, unique=True, nullable=True)

    moods = relationship("MoodEntry", back_populates="user", cascade="all, delete-orphan")
    journals = relationship("JournalEntry", back_populates="user", cascade="all, delete-orphan")
    completed_activities = relationship(
        "CompletedActivity", back_populates="user", cascade="all, delete-orphan"
    )
