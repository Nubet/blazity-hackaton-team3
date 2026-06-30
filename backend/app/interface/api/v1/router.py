from fastapi import APIRouter

from app.interface.api.v1 import uploads

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(uploads.router)
