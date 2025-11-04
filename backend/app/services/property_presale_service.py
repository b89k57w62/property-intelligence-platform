"""Property presale business logic service"""

from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.repositories.property_presale_repository import PropertyPresaleRepository
from app.schemas.property_presale import (
    PropertyPresaleResponse,
    PropertyPresaleSearchResponse,
)


class PropertyPresaleService:
    """Service layer for property presale business logic."""

    def __init__(self, db: Session):
        """Initialize service with database session."""
        self.repository = PropertyPresaleRepository(db)

    def get_by_id(self, property_id: int) -> Optional[PropertyPresaleResponse]:
        """Get a single presale by ID."""
        property_orm = self.repository.get(property_id)

        if property_orm is None:
            return None

        return PropertyPresaleResponse.model_validate(property_orm)

    def search(
        self, filters: Optional[Dict[str, Any]] = None, skip: int = 0, limit: int = 20
    ) -> PropertyPresaleSearchResponse:
        """Search presales with filters and pagination."""
        if filters is None:
            filters = {}

        result = self.repository.search(**filters, skip=skip, limit=limit)

        items = [
            PropertyPresaleResponse.model_validate(item) for item in result["items"]
        ]

        return PropertyPresaleSearchResponse(
            total=result["total"],
            items=items,
            page=result["page"],
            page_size=result["page_size"],
            total_pages=result["total_pages"],
        )
