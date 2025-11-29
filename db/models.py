from sqlmodel import Field, SQLModel, Relationship, select
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    major: str
    graduation_year: int

class LostItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    location_found: str
    contact: str


class PrayerRequest(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    prayer_request: str
    posted_by: str
    is_anonymous: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)