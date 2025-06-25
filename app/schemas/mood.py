from datetime import datetime

from pydantic import BaseModel


class MoodBase(BaseModel):
    mood: str
    note: str | None = None


class MoodCreate(MoodBase):
    pass


class MoodRead(MoodBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        orm_mode = True
