"""API v1 router configuration."""

from fastapi import APIRouter

# Import endpoint routers here
# from app.api.v1.endpoints import properties, health

api_router = APIRouter()

# Include endpoint routers
# api_router.include_router(health.router, prefix="/health", tags=["health"])
# api_router.include_router(properties.router, prefix="/properties", tags=["properties"])
