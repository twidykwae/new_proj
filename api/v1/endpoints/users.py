from fastapi import APIRouter, HTTPException, Query, Response
from db.models import User
from db.session import SessionDep, select
from sqlmodel import func
from db.models import User


router = APIRouter()

#Create route for GET ALL USERS with pagination
@router.get("/")
def get_all_users(response: Response, session: SessionDep, curPage: int = Query(1, ge=1), pageSize: int = Query(10, ge=1)):
    offset_value = (curPage - 1) * pageSize
    statement = select(User).order_by(User.id).offset(offset_value).limit(pageSize)
    users = session.exec(statement).all()
    total_count = total_count = session.exec(select(func.count()).select_from(User)).one()

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

@router.post("/", status_code=204)
def create_new_user(user: User, session: SessionDep):
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