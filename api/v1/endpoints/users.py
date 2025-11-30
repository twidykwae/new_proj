from fastapi import APIRouter, HTTPException, Depends, Response, status, FastAPI
from db.models import User
from db.session import SessionDep, select, get_session
from sqlmodel import col
from sqlmodel import func
from db.models import User
import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
import jwt


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '30'))

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User


router = APIRouter()


password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/token")


def verify_password(password, hashed_password):
    return password_hash.verify(password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)


def get_user_by_email(email: str):
    for session in get_session():
        return session.exec(select(User).where(User.email == email)).first()
    

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_email(username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user


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
    return Token(access_token=access_token, token_type="bearer", user=user)


@router.get("/me", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user



#Create route for GET ALL USERS with pagination
@router.get("/")
def get_all_users(response: Response, session: SessionDep, curPage: int = 1, pageSize: int = 10, searchText: str=""):
    offset_value = (curPage - 1) * pageSize
    
    statement = select(User)
    
    # Search across multiple fields
    if searchText:
        statement = statement.where(
            col(User.name).ilike(f"%{searchText}%") | 
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
def get_user(user_id:int, session: SessionDep):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", status_code=201)
def create_new_user(user: User, session: SessionDep):
    user.password = get_password_hash(user.password)
    new_user = user
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.delete("/{user_id}", status_code=204)
def delete_user(session: SessionDep, user_id: int):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return