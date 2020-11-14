from fastapi import FastAPI

from .routes import item_router

app = FastAPI()
app.include_router(item_router, prefix="/items")
