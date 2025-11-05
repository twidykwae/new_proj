from fastapi import APIRouter, HTTPException
from db.models import User
from db.session import SessionDep, select
from db.models import User

router = APIRouter()


@router.get("/")
def get_all_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return users
    
#Create route for GET USER
@router.get("/{user_id}")
def get_user(user_id:int, session: SessionDep):
    user = session.exec(User).get(user_id)
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