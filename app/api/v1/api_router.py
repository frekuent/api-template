from fastapi import APIRouter

from app.api.v1.routes import item_routes

api_router = APIRouter()
api_router.include_router(item_routes.router, prefix="/items", tags=["items"])
