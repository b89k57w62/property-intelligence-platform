"""Property presale API endpoints"""

from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.property_presale_service import PropertyPresaleService
from app.schemas.property_presale import (
    PropertyPresaleResponse,
    PropertyPresaleSearchResponse,
)

router = APIRouter()


@router.get("/{property_id}", response_model=PropertyPresaleResponse)
def get_presale(property_id: int, db: Session = Depends(get_db)):
    """Get single presale by ID."""
    service = PropertyPresaleService(db)
    result = service.get_by_id(property_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Presale with ID {property_id} not found",
        )

    return result


@router.get("/", response_model=PropertyPresaleSearchResponse)
def search_presales(
    city: Optional[str] = Query(None, description="City name"),
    district: Optional[str] = Query(None, description="District name"),
    project_name: Optional[str] = Query(
        None, description="Project name (fuzzy search)"
    ),
    date_from: Optional[str] = Query(None, description="Start date (ROC format)"),
    date_to: Optional[str] = Query(None, description="End date (ROC format)"),
    price_min: Optional[int] = Query(None, description="Minimum total price (NTD)"),
    price_max: Optional[int] = Query(None, description="Maximum total price (NTD)"),
    building_types: Optional[List[str]] = Query(None, description="Building types"),
    skip: int = Query(0, ge=0, description="Records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Max records to return"),
    db: Session = Depends(get_db),
):
    """Search presales with filters."""
    service = PropertyPresaleService(db)

    filters = {
        "city": city,
        "district": district,
        "project_name": project_name,
        "date_from": date_from,
        "date_to": date_to,
        "price_min": price_min,
        "price_max": price_max,
        "building_types": building_types,
    }

    filters = {k: v for k, v in filters.items() if v is not None}

    return service.search(filters=filters, skip=skip, limit=limit)
