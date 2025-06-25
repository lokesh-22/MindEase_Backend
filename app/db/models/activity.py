from sqlalchemy import Column, String

from app.db.database import Base


class ActivitySuggestion(Base):
    __tablename__ = "activity_suggestions"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)
    tags = Column(String, nullable=True)  # Comma-separated tags
