"""Property rental business logic service"""

from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.repositories.property_rental_repository import PropertyRentalRepository
from app.schemas.property_rental import (
    PropertyRentalResponse,
    PropertyRentalSearchResponse,
)


class PropertyRentalService:
    """Service layer for property rental business logic."""

    def __init__(self, db: Session):
        """Initialize service with database session."""
        self.repository = PropertyRentalRepository(db)

    def get_by_id(self, property_id: int) -> Optional[PropertyRentalResponse]:
        """Get a single rental by ID."""
        property_orm = self.repository.get(property_id)

        if property_orm is None:
            return None

        return PropertyRentalResponse.model_validate(property_orm)

    def search(
        self, filters: Optional[Dict[str, Any]] = None, skip: int = 0, limit: int = 20
    ) -> PropertyRentalSearchResponse:
        """Search rentals with filters and pagination."""
        if filters is None:
            filters = {}

        result = self.repository.search(**filters, skip=skip, limit=limit)

        items = [
            PropertyRentalResponse.model_validate(item) for item in result["items"]
        ]

        return PropertyRentalSearchResponse(
            total=result["total"],
            items=items,
            page=result["page"],
            page_size=result["page_size"],
            total_pages=result["total_pages"],
        )
