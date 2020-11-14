from http import HTTPStatus
from typing import Optional, Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .routes import item_router


app = FastAPI()
app.include_router(item_router, prefix="/items")

