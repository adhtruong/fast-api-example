from typing import Generic, List, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel


class Message(BaseModel):
    message: str


_DataType = TypeVar("_DataType", bound=BaseModel)


class Response(GenericModel, Generic[_DataType]):
    count: int
    data: List[_DataType]
