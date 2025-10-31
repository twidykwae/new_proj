from fastapi import APIRouter, HTTPException
from db.models import LostItem

router = APIRouter()

@router.get("/")
def get_all_lost_items():
    # Add code to get all lost items from DB
    return {"message": "Lost items listed"}

#Create route for GET LOST ITEM
@router.get("/{item_id}")
def get_lost_item(item_id:int):
    #Add code to get lost item from DB
    lost_item = None
    if not lost_item:
        raise HTTPException(status_code=404, detail="Lost item not found")
    return lost_item

@router.post("/", status_code=204)
def create_new_lost_item(lost_item: LostItem):
    #Add code to create the lost item
    new_lost_item = lost_item
    return new_lost_item