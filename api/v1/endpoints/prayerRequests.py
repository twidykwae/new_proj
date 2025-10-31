from fastapi import APIRouter, HTTPException
from db.models import PrayerRequest

router = APIRouter()

@router.get("/")
def get_all_prayer_requests():
    return {"message": "Prayer requests listed"}

@router.get("/{request_id}")
def get_prayer_request(request_id: int):
    # Add code to get prayer request from DB
    prayer_request = None
    if not prayer_request:
        raise HTTPException(status_code=404, detail="Prayer request not found")
    return prayer_request

@router.post("/", status_code=204)
def create_new_prayer_request(prayer_request: PrayerRequest):
    # Add code to create the prayer request
    new_prayer_request = prayer_request
    return new_prayer_request