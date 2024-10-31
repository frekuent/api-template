# app/routes.py
from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health")
def health_check():
    return {"status": "healthy"}


@api_router.get("/status")
def status_check():
    return {"status": "running"}
