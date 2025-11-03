"""API v1 router configuration."""

from fastapi import APIRouter
from app.api.v1.endpoints import properties

api_router = APIRouter()

# Register property endpoints
api_router.include_router(properties.router, prefix="/properties", tags=["properties"])
