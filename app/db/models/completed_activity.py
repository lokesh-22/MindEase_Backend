from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class CompletedActivity(Base):
    __tablename__ = "completed_activities"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    activity_id = Column(String, ForeignKey("activity_suggestions.id"), nullable=False)
    rating = Column(String, nullable=True)
    note = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="completed_activities")
    activity = relationship("ActivitySuggestion")
