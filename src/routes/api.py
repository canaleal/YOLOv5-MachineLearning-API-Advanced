from fastapi import APIRouter
from src.endpoints import google, dashcam

router = APIRouter()
router.include_router(google.router)
router.include_router(dashcam.router)