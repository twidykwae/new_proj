from fastapi import APIRouter
from api.v1.endpoints import users, lostItems, prayerRequests


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(lostItems.router, prefix="/lost-items", tags=["Lost Items"])
api_router.include_router(prayerRequests.router, prefix="/prayer-requests", tags=["Prayer Requests"])