"""Property Rental Repository"""

from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from app.models.property_rental import PropertyRental
from app.repositories.base import BaseRepository


class PropertyRentalRepository(BaseRepository[PropertyRental]):
    """Repository for property rental data access."""

    def __init__(self, db: Session):
        """Initialize repository with database session."""
        super().__init__(PropertyRental, db)

    def get_by_id(self, property_id: int) -> Optional[PropertyRental]:
        """Get rental by ID."""
        return self.get(property_id)

    def get_by_location(
        self, city: str, district: Optional[str] = None, skip: int = 0, limit: int = 20
    ) -> List[PropertyRental]:
        """Get rentals by location with pagination."""
        query = self.db.query(self.model).filter(self.model.city == city)

        if district:
            query = query.filter(self.model.district == district)

        return query.offset(skip).limit(limit).all()

    def search(
        self,
        city: Optional[str] = None,
        district: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        rent_min: Optional[int] = None,
        rent_max: Optional[int] = None,
        building_types: Optional[List[str]] = None,
        has_elevator: Optional[bool] = None,
        has_furniture: Optional[bool] = None,
        skip: int = 0,
        limit: int = 20,
        order_by: str = "rental_date",
        order_desc: bool = True,
    ) -> Dict[str, Any]:
        """Search rentals with filters."""
        query = self.db.query(self.model)

        if city:
            query = query.filter(self.model.city == city)
        if district:
            query = query.filter(self.model.district == district)
        if date_from:
            query = query.filter(self.model.rental_date >= date_from)
        if date_to:
            query = query.filter(self.model.rental_date <= date_to)
        if rent_min:
            query = query.filter(self.model.monthly_rent_ntd >= rent_min)
        if rent_max:
            query = query.filter(self.model.monthly_rent_ntd <= rent_max)
        if building_types:
            query = query.filter(self.model.building_type.in_(building_types))
        if has_elevator is not None:
            query = query.filter(self.model.has_elevator == has_elevator)
        if has_furniture is not None:
            query = query.filter(self.model.has_furniture == has_furniture)

        order_column = getattr(self.model, order_by, self.model.rental_date)
        query = query.order_by(
            order_column.desc() if order_desc else order_column.asc()
        )

        total = query.count()
        items = query.offset(skip).limit(limit).all()

        return {
            "total": total,
            "items": items,
            "page": (skip // limit) + 1,
            "page_size": limit,
            "total_pages": (total + limit - 1) // limit,
        }
