from datetime import datetime

from pydantic import BaseModel


class CompletedActivityBase(BaseModel):
    activity_id: str
    rating: str | None = None
    note: str | None = None


class CompletedActivityCreate(CompletedActivityBase):
    pass


class CompletedActivityRead(CompletedActivityBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        orm_mode = True
