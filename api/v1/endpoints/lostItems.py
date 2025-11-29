from fastapi import APIRouter, HTTPException, Response
from sqlalchemy import func
from sqlmodel import col
from db.models import LostItem
from db.session import SessionDep, select

router = APIRouter()

@router.get("/")
def get_all_lost_items(response: Response,session: SessionDep,curPage: int = 1,pageSize: int = 10,searchText: str = ""):
    offset_value = (curPage - 1) * pageSize

    query = select(LostItem)

    if searchText:
        search = f"%{searchText}%"
        query = query.where(
            LostItem.title.ilike(search) |
            LostItem.description.ilike(search) |
            LostItem.location_found.ilike(search)
        )

    total = session.exec(
        select(func.count()).select_from(query.subquery())
    ).one()

    items = session.exec(
        query.order_by(LostItem.id).offset(offset_value).limit(pageSize)
    ).all()

    return {
        "total": total,
        "items": items
    }

    

#Create route for GET LOST ITEM
@router.get("/{item_id}")
def get_lost_item(item_id:int, session: SessionDep):
    #Add code to get lost item from DB
    lost_item = session.exec(select(LostItem).where(LostItem.id == item_id)).first()
    if not lost_item:
        raise HTTPException(status_code=404, detail="Lost item not found")
    return lost_item

@router.post("/", status_code=201)
def create_new_lost_item(lost_item: LostItem, session: SessionDep):
    #Add code to create the lost item
    new_lost_item = lost_item
    session.add(new_lost_item)
    session.commit()
    session.refresh(new_lost_item)
    return new_lost_item

@router.put("/{item_id}")
def update_lost_item(item_id: int, lost_item: LostItem, session: SessionDep):
    #Add code to update lost item in DB
    existing_item = session.exec(select(LostItem).where(LostItem.id == item_id)).first()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Lost item not found")
    existing_item.title = lost_item.title
    existing_item.description = lost_item.description
    existing_item.location_found = lost_item.location_found
    existing_item.contact = lost_item.contact
    session.add(existing_item)
    session.commit()
    session.refresh(existing_item)
    return existing_item


@router.delete("/{item_id}")
def delete_lost_item(session: SessionDep, item_id: int):
    #Add code to delete lost item from DB
    lost_item = session.exec(select(LostItem).where(LostItem.id == item_id)).first()
    if not lost_item:
        raise HTTPException(status_code=404, detail="Lost item not found")
    session.delete(lost_item)
    session.commit()