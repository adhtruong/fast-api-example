from fastapi import APIRouter, HTTPException

from app.models.items import Item, ItemList
from app.models.message import Message

item_router = APIRouter()

ITEMS = {i: Item(id=i, name=f"Item {i}") for i in range(1, 10)}


@item_router.get("/", response_model=ItemList)
def get_all_items():
    return {"count": len(ITEMS), "data": list(ITEMS.values())}


@item_router.get("/{item_id}", response_model=Item, responses={404: {"model": Message}})
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")

    return ITEMS[item_id]
