"""Property Presale Repository"""

from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from app.models.property_presale import PropertyPresale
from app.repositories.base import BaseRepository


class PropertyPresaleRepository(BaseRepository[PropertyPresale]):
    """Repository for property presale data access."""

    def __init__(self, db: Session):
        """Initialize repository with database session."""
        super().__init__(PropertyPresale, db)

    def get_by_id(self, property_id: int) -> Optional[PropertyPresale]:
        """Get presale by ID."""
        return self.get(property_id)

    def get_by_location(
        self, city: str, district: Optional[str] = None, skip: int = 0, limit: int = 20
    ) -> List[PropertyPresale]:
        """Get presales by location with pagination."""
        query = self.db.query(self.model).filter(self.model.city == city)

        if district:
            query = query.filter(self.model.district == district)

        return query.offset(skip).limit(limit).all()

    def search(
        self,
        city: Optional[str] = None,
        district: Optional[str] = None,
        project_name: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        building_types: Optional[List[str]] = None,
        skip: int = 0,
        limit: int = 20,
        order_by: str = "transaction_date",
        order_desc: bool = True,
    ) -> Dict[str, Any]:
        """Search presales with filters."""
        query = self.db.query(self.model)

        if city:
            query = query.filter(self.model.city == city)
        if district:
            query = query.filter(self.model.district == district)
        if project_name:
            query = query.filter(self.model.project_name.like(f"%{project_name}%"))
        if date_from:
            query = query.filter(self.model.transaction_date >= date_from)
        if date_to:
            query = query.filter(self.model.transaction_date <= date_to)
        if price_min:
            query = query.filter(self.model.total_price_ntd >= price_min)
        if price_max:
            query = query.filter(self.model.total_price_ntd <= price_max)
        if building_types:
            query = query.filter(self.model.building_type.in_(building_types))

        order_column = getattr(self.model, order_by, self.model.transaction_date)
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
