"""API v1 router configuration."""

from fastapi import APIRouter
from app.api.v1.endpoints import (
    property_transactions,
    property_presales,
    property_rentals,
)

api_router = APIRouter()

# Register property endpoints
api_router.include_router(
    property_transactions.router, prefix="/transactions", tags=["transactions"]
)
api_router.include_router(
    property_presales.router, prefix="/presales", tags=["presales"]
)
api_router.include_router(property_rentals.router, prefix="/rentals", tags=["rentals"])
