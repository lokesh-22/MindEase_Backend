from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# -------------------
# User Schemas
# -------------------

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    anonymous_id: str

    class Config:
        orm_mode = True


# -------------------
# Auth Token Schema
# -------------------

class Token(BaseModel):
    access_token: str
    token_type: str


# -------------------
# Journal Entry Schemas
# -------------------

class JournalEntryCreate(BaseModel):
    title: str
    content: str


class JournalEntryOut(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True


class JournalEntryUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

    class Config:
        orm_mode = True


class JournalEntryList(BaseModel):
    entries: List[JournalEntryOut]

    class Config:
        orm_mode = True
