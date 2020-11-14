from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class ItemList(BaseModel):
    count: int
    data: List[Item]


class Message(BaseModel):
    message: str