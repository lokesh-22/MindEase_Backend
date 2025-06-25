from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class MoodEntry(Base):
    __tablename__ = "mood_entries"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    mood = Column(String, nullable=False)
    note = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="moods")
