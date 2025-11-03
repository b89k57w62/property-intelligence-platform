"""Property business logic service."""

from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.repositories.property_repository import PropertyRepository
from app.schemas.property import PropertyResponse, PropertySearchResponse


class PropertyService:
    """
    Property Service - Business logic layer.

    Responsibilities:
    - Orchestrate repository operations
    - Apply business rules and validations
    - Convert ORM models to DTOs
    - Handle service-level errors

    Note: Following Dependency Inversion Principle - depends on abstractions (Repository interface)
    """

    def __init__(self, db: Session):
        """
        Initialize PropertyService with database session.

        Args:
            db: SQLAlchemy database session

        Example:
            service = PropertyService(db)
        """
        self.repository = PropertyRepository(db)

    def get_by_id(self, property_id: int) -> Optional[PropertyResponse]:
        """
        Get a single property by ID.

        Args:
            property_id: Property ID to retrieve

        Returns:
            PropertyResponse DTO if found, None if not found

        Example:
            property_dto = service.get_by_id(123)
            if property_dto:
                print(f"Found: {property_dto.city}")
            else:
                print("Property not found")
        """
        # Get ORM object from repository
        property_orm = self.repository.get(property_id)

        if property_orm is None:
            return None

        # Convert ORM to DTO
        return PropertyResponse.model_validate(property_orm)

    def search_properties(
        self, filters: Optional[Dict[str, Any]] = None, skip: int = 0, limit: int = 20
    ) -> PropertySearchResponse:
        """
        Search properties with filters and pagination.

        Args:
            filters: Dictionary of filter parameters (city, district, price_range, etc.)
            skip: Number of records to skip for pagination
            limit: Maximum number of records to return

        Returns:
            PropertySearchResponse with paginated results and metadata

        Example:
            result = service.search_properties(
                filters={
                    "city": "台北市",
                    "has_elevator": True,
                    "total_price_min": 5000000,
                    "total_price_max": 15000000
                },
                skip=0,
                limit=20
            )
            print(f"Found {result.total} properties")
            for prop in result.items:
                print(f"{prop.city} {prop.district}: NT${prop.total_price_ntd}")
        """
        # Prepare filters, default to empty dict
        if filters is None:
            filters = {}

        # Add pagination to filters
        filters["skip"] = skip
        filters["limit"] = limit

        # Call repository search (returns dict with ORM items)
        result = self.repository.search(**filters)

        # Convert ORM items to DTOs
        dto_items = [PropertyResponse.model_validate(item) for item in result["items"]]

        # Return DTO response with converted items
        return PropertySearchResponse(
            total=result["total"],
            items=dto_items,
            page=result["page"],
            page_size=result["page_size"],
            total_pages=result["total_pages"],
        )
