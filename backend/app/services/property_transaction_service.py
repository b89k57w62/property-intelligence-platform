"""Property transaction business logic service"""

from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.repositories.property_transaction_repository import (
    PropertyTransactionRepository,
)
from app.schemas.property_transaction import (
    PropertyTransactionResponse,
    PropertyTransactionSearchResponse,
)


class PropertyTransactionService:
    """Service layer for property transaction business logic."""

    def __init__(self, db: Session):
        """Initialize service with database session."""
        self.repository = PropertyTransactionRepository(db)

    def get_by_id(self, property_id: int) -> Optional[PropertyTransactionResponse]:
        """Get a single transaction by ID."""
        property_orm = self.repository.get(property_id)

        if property_orm is None:
            return None

        return PropertyTransactionResponse.model_validate(property_orm)

    def search(
        self, filters: Optional[Dict[str, Any]] = None, skip: int = 0, limit: int = 20
    ) -> PropertyTransactionSearchResponse:
        """Search transactions with filters and pagination."""
        if filters is None:
            filters = {}

        result = self.repository.search(**filters, skip=skip, limit=limit)

        items = [
            PropertyTransactionResponse.model_validate(item) for item in result["items"]
        ]

        return PropertyTransactionSearchResponse(
            total=result["total"],
            items=items,
            page=result["page"],
            page_size=result["page_size"],
            total_pages=result["total_pages"],
        )
