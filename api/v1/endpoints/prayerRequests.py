from fastapi import APIRouter, HTTPException, Response
from sqlmodel import col, func
from db.models import PrayerRequest
from db.session import SessionDep, select

router = APIRouter()

@router.get("/")
def get_all_prayer_requests(response: Response, session: SessionDep, curPage: int = 1, pageSize: int = 10, searchText: str=""):
    # Add code to get all prayer requests from DB
    offset_value = (curPage - 1) * pageSize
    statement = select(PrayerRequest).order_by(PrayerRequest.id).offset(offset_value).limit(pageSize)
    searchStatement = select(PrayerRequest).where(col(PrayerRequest.title).ilike(f"%{searchText}%"))
    search = session.exec(searchStatement)
    prayers = session.exec(statement).all()
    total_count = total_count = session.exec(select(func.count()).select_from(PrayerRequest)).one()
    return {
        "total": total_count,
        "prayers": prayers,
        "search": search
    }

@router.get("/{request_id}")
def get_prayer_request(request_id: int, session: SessionDep):
    # Add code to get prayer request from DB
    prayer_request = session.exec(select(PrayerRequest).where(PrayerRequest.id == request_id)).first()
    if not prayer_request:
        raise HTTPException(status_code=404, detail="Prayer request not found")
    return prayer_request

@router.post("/", status_code=201)
def create_new_prayer_request(prayer_request: PrayerRequest, session: SessionDep):
    new_prayer_request = prayer_request
    session.add(new_prayer_request)
    session.commit()
    session.refresh(new_prayer_request)
    return new_prayer_request

@router.delete("/{request_id}")
def delete_prayer_request(session: SessionDep, request_id: int):
    prayer_request = session.exec(select(PrayerRequest).where(PrayerRequest.id == request_id)).first()
    if not prayer_request:
        raise HTTPException(status_code=404, detail="Prayer request not found")
    session.delete(prayer_request)
    session.commit()
    return {"detail": "Prayer request deleted"}

@router.put("/{request_id}")
def update_prayer_request(request_id: int, prayer_request: PrayerRequest, session: SessionDep):
    existing_request = session.exec(select(PrayerRequest).where(PrayerRequest.id == request_id)).first()
    if not existing_request:
        raise HTTPException(status_code=404, detail="Prayer request not found")
    existing_request.title = prayer_request.title
    existing_request.prayer_request = prayer_request.prayer_request
    existing_request.posted_by = prayer_request.posted_by
    existing_request.is_anonymous = prayer_request.is_anonymous
    session.add(existing_request)
    session.commit()
    session.refresh(existing_request)
    return existing_request

