from datetime import datetime

from pydantic import BaseModel


class JournalBase(BaseModel):
    title: str
    content: str


class JournalCreate(JournalBase):
    pass


class JournalRead(JournalBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        orm_mode = True
