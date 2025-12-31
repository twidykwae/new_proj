from fastapi import APIRouter, HTTPException, Depends, Response, status, FastAPI
from db.models import UserBase as User
from db.session import SessionDep, select, get_session
from sqlmodel import col
from sqlmodel import func
from db.schemas import Token, UserRead, PaginatedUsers, UserCreate
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from fastapi.middleware.cors import CORSMiddleware

from core.security import(
    ACCESS_TOKEN_EXPIRE_MINUTES,
    verify_password,
    get_password_hash,
    get_user_by_email,
    authenticate_user,
    create_access_token,
    get_current_user,
    get_current_active_user,
    get_current_active_admin_user
)

router = APIRouter()


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer", user=UserRead.model_validate(user))


@router.get("/me", response_model=UserRead)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return UserRead.model_validate(current_user)



#Create route for GET ALL USERS with pagination
@router.get("/", response_model=PaginatedUsers)
def get_all_users(response: Response, current_user: Annotated[User, Depends(get_current_active_admin_user)], session: SessionDep, curPage: int = 1, pageSize: int = 10, searchText: str=""):
    offset_value = (curPage - 1) * pageSize
    statement = select(User)
    
    if searchText:
        statement = statement.where(
            col(User.full_name).ilike(f"%{searchText}%") | 
            col(User.email).ilike(f"%{searchText}%") |
            col(User.major).ilike(f"%{searchText}%")
        )
    
    total_count = session.exec(select(func.count()).select_from(statement.subquery())).one()
    statement = statement.order_by(User.id).offset(offset_value).limit(pageSize)
    users = session.exec(statement).all()

    return {
        "total": total_count,
        "users": users
    }
    
#Create route for GET USER
@router.get("/{user_id}")
def get_user(user_id:int, current_user: Annotated[User, Depends(get_current_active_user)], session: SessionDep):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", status_code=201)
def create_new_user(user: UserCreate, session: SessionDep):
    if session.exec(select(User).where(User.email == user.email)).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if len(user.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    
    # Create User instance from UserCreate schema
    hashed_password = get_password_hash(user.password)
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        major=user.major,
        graduation_year=user.graduation_year,
        profile_image_url=user.profile_image_url,
        is_admin=False
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.delete("/{user_id}", status_code=204)
def delete_user(session: SessionDep, user_id: int, current_user: Annotated[User, Depends(get_current_active_admin_user)]):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return

