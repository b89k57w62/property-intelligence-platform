"""Property rental API endpoints"""

from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.property_rental_service import PropertyRentalService
from app.schemas.property_rental import (
    PropertyRentalResponse,
    PropertyRentalSearchResponse,
)

router = APIRouter()


@router.get("/{property_id}", response_model=PropertyRentalResponse)
def get_rental(property_id: int, db: Session = Depends(get_db)):
    """Get single rental by ID."""
    service = PropertyRentalService(db)
    result = service.get_by_id(property_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rental with ID {property_id} not found",
        )

    return result


@router.get("/", response_model=PropertyRentalSearchResponse)
def search_rentals(
    city: Optional[str] = Query(None, description="City name"),
    district: Optional[str] = Query(None, description="District name"),
    date_from: Optional[str] = Query(None, description="Start date (ROC format)"),
    date_to: Optional[str] = Query(None, description="End date (ROC format)"),
    rent_min: Optional[int] = Query(None, description="Minimum monthly rent (NTD)"),
    rent_max: Optional[int] = Query(None, description="Maximum monthly rent (NTD)"),
    building_types: Optional[List[str]] = Query(None, description="Building types"),
    has_elevator: Optional[bool] = Query(None, description="Has elevator"),
    has_furniture: Optional[bool] = Query(None, description="Has furniture"),
    skip: int = Query(0, ge=0, description="Records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Max records to return"),
    db: Session = Depends(get_db),
):
    """Search rentals with filters."""
    service = PropertyRentalService(db)

    filters = {
        "city": city,
        "district": district,
        "date_from": date_from,
        "date_to": date_to,
        "rent_min": rent_min,
        "rent_max": rent_max,
        "building_types": building_types,
        "has_elevator": has_elevator,
        "has_furniture": has_furniture,
    }

    filters = {k: v for k, v in filters.items() if v is not None}

    return service.search(filters=filters, skip=skip, limit=limit)
