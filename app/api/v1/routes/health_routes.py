from fastapi import APIRouter

from app.services.health_service import check_health, check_status

router = APIRouter()


@router.get("/health", tags=["system"])
def health_check():
    return check_health()


@router.get("/status", tags=["system"])
def status_check():
    return check_status()
