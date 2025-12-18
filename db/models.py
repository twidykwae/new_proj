from sqlmodel import Field, SQLModel, Relationship, select
from datetime import datetime
from sqlalchemy import Column, String
from pydantic import HttpUrl, EmailStr

class UserBase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    email: str
    password: str
    major: str
    graduation_year: int
    profile_image_url: HttpUrl | None = Field(default=None, sa_column=Column(String(2048)))
    is_admin: bool = False


class RoommateProfile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userbase.id")
    gender: str
    bio: str
    preferences: str
    housing_type: str   
    sleep_schedule: str
    looking_for: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class LostandFoundItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    category: str
    contact: str
    location_found: str
    date_found: datetime = Field(default_factory=datetime.utcnow)
    image_url: HttpUrl | None = Field(default=None, sa_column=Column(String(2048)))
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PrayerRequest(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    prayer_request: str
    is_anonymous: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class PrayerInteractionModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    prayer_request_id: int = Field(foreign_key="prayerrequest.id")
    user_id: int = Field(foreign_key="userbase.id")
    interaction_type: str  # e.g., "prayed", "commented"
    created_at: datetime = Field(default_factory=datetime.utcnow)