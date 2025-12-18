from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import BaseModel, HttpUrl, EmailStr

class UserCreate(SQLModel):
    full_name: str
    email: EmailStr
    password: str
    major: str
    graduation_year: int
    profile_image_url: HttpUrl | None = None

class UserRead(SQLModel):
    id: int
    full_name: str
    email: EmailStr
    major: str
    graduation_year: int
    is_admin: bool = Field(default=False)
    profile_image_url: HttpUrl | None = None

class UserUpdate(SQLModel):
    full_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    major: str | None = None
    graduation_year: int | None = None
    profile_image_url: HttpUrl | None = None

class LostandFoundItemCreate(SQLModel):
    title: str
    description: str
    category: str
    contact: str
    location_found: str
    image_url: str | None = None

class LostandFoundItemRead(SQLModel):
    id: int
    title: str
    description: str
    category: str
    contact: str
    location_found: str
    date_found: datetime
    image_url: str | None = None
    created_at: datetime

class LostandFoundItemUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    contact: str | None = None
    location_found: str | None = None
    image_url: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserRead

class PrayerRequestCreate(SQLModel):
    title: str
    prayer_request: str
    is_anonymous: bool = True

class PrayerRequestRead(SQLModel):
    id: int
    title: str
    prayer_request: str
    is_anonymous: bool
    created_at: datetime

class PrayerRequestUpdate(SQLModel):
    title: str | None = None
    prayer_request: str | None = None
    is_anonymous: bool | None = None


class PaginatedUsers(BaseModel):
    total: int
    users: list[UserRead]
