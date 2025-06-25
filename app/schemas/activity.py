from pydantic import BaseModel


class ActivitySuggestionBase(BaseModel):
    title: str
    description: str | None = None
    category: str | None = None
    tags: str | None = None


class ActivitySuggestionCreate(ActivitySuggestionBase):
    pass


class ActivitySuggestionRead(ActivitySuggestionBase):
    id: str

    class Config:
        orm_mode = True
