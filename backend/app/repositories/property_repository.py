"""Property Repository - Property data access layer"""

from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from app.models.property import Property
from app.repositories.base import BaseRepository


class PropertyRepository(BaseRepository[Property]):
    """
    Property Repository

    Handles all database operations for Property model.
    Inherits basic CRUD from BaseRepository.
    """

    def __init__(self, db: Session):
        """
        Initialize Property Repository

        Args:
            db: SQLAlchemy Session instance
        """
        super().__init__(Property, db)

    def get_by_id(self, property_id: int) -> Optional[Property]:
        """
        Query property by ID

        Args:
            property_id: Property primary key ID

        Returns:
            Property instance if found, None otherwise
        """
        return self.get(property_id)

    def get_by_location(
        self, city: str, district: Optional[str] = None, skip: int = 0, limit: int = 20
    ) -> List[Property]:
        """
        Query properties by location

        Args:
            city: City name (required)
            district: District name (optional)
            skip: Number of records to skip for pagination (default: 0)
            limit: Maximum number of records to return (default: 20)

        Returns:
            List of Property instances

        Example:
            # Query all properties in Taipei
            properties = repo.get_by_location(city="台北市")

            # Query properties in specific district
            properties = repo.get_by_location(city="台北市", district="大安區")

            # Query with pagination (page 2, 20 items per page)
            properties = repo.get_by_location(city="台北市", skip=20, limit=20)
        """
        query = self.db.query(self.model).filter(self.model.city == city)

        if district:
            query = query.filter(self.model.district == district)

        return query.offset(skip).limit(limit).all()

    def search(
        self,
        # ==================== Basic Filters ====================
        city: Optional[str] = None,
        district: Optional[str] = None,
        transaction_targets: Optional[List[str]] = None,
        address_keyword: Optional[str] = None,
        # ==================== Date Range ====================
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        # ==================== Price Range ====================
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        total_price_min: Optional[int] = None,
        total_price_max: Optional[int] = None,
        # ==================== Area Range ====================
        area_min: Optional[float] = None,
        area_max: Optional[float] = None,
        main_area_min: Optional[float] = None,
        main_area_max: Optional[float] = None,
        # ==================== Building Filters ====================
        building_types: Optional[List[str]] = None,
        main_usages: Optional[List[str]] = None,
        urban_land_uses: Optional[List[str]] = None,
        # ==================== Special Conditions ====================
        has_elevator: Optional[bool] = None,
        has_management: Optional[bool] = None,
        has_note: Optional[bool] = None,
        # ==================== Floor Range ====================
        floor_min: Optional[int] = None,
        floor_max: Optional[int] = None,
        # ==================== Layout ====================
        room_count: Optional[int] = None,
        living_count: Optional[int] = None,
        bathroom_count: Optional[int] = None,
        # ==================== Pagination & Sorting ====================
        skip: int = 0,
        limit: int = 20,
        order_by: str = "transaction_date",
        order_desc: bool = True,
    ) -> Dict[str, Any]:
        """
        Complex search with multiple filters

        This is the core search method supporting all filter conditions
        from the Taiwan real estate registration website.

        Args:
            city: City name filter
            district: District name filter
            transaction_targets: List of transaction targets (房地/建物/土地/車位)
            address_keyword: Keyword to search in address
            date_from: Start date in ROC format (YYYMMDD, e.g., "1130101")
            date_to: End date in ROC format (YYYMMDD, e.g., "1141231")
            price_min: Minimum unit price (NTD per sqm)
            price_max: Maximum unit price (NTD per sqm)
            total_price_min: Minimum total price (NTD)
            total_price_max: Maximum total price (NTD)
            area_min: Minimum building area (sqm)
            area_max: Maximum building area (sqm)
            main_area_min: Minimum main building area (sqm)
            main_area_max: Maximum main building area (sqm)
            building_types: List of building types
            main_usages: List of main usages
            urban_land_uses: List of urban land uses
            has_elevator: Filter by elevator availability
            has_management: Filter by management organization availability
            has_note: Filter by presence of notes
            floor_min: Minimum floor number
            floor_max: Maximum floor number
            room_count: Number of rooms
            living_count: Number of living rooms
            bathroom_count: Number of bathrooms
            skip: Number of records to skip for pagination
            limit: Maximum number of records to return
            order_by: Field name to sort by (default: "transaction_date")
            order_desc: Sort in descending order (default: True)

        Returns:
            Dictionary containing:
            - total: Total number of matching records
            - items: List of Property instances
            - page: Current page number
            - page_size: Number of items per page
            - total_pages: Total number of pages

        Example:
            # Search properties in Taipei Da'an District with elevator
            result = repo.search(
                city="台北市",
                district="大安區",
                has_elevator=True,
                skip=0,
                limit=20
            )
            print(f"Found {result['total']} properties")
            for prop in result['items']:
                print(prop.address, prop.total_price_ntd)
        """
        query = self.db.query(self.model)

        if city:
            query = query.filter(self.model.city == city)

        if district:
            query = query.filter(self.model.district == district)

        if transaction_targets:
            query = query.filter(self.model.transaction_target.in_(transaction_targets))

        if address_keyword:
            query = query.filter(self.model.land_section.like(f"%{address_keyword}%"))

        if date_from:
            query = query.filter(self.model.transaction_date >= date_from)
        if date_to:
            query = query.filter(self.model.transaction_date <= date_to)

        if price_min:
            query = query.filter(self.model.unit_price_ntd >= price_min)
        if price_max:
            query = query.filter(self.model.unit_price_ntd <= price_max)

        if total_price_min:
            query = query.filter(self.model.total_price_ntd >= total_price_min)
        if total_price_max:
            query = query.filter(self.model.total_price_ntd <= total_price_max)

        if area_min:
            query = query.filter(self.model.building_area_sqm >= area_min)
        if area_max:
            query = query.filter(self.model.building_area_sqm <= area_max)

        if main_area_min:
            query = query.filter(self.model.main_building_area >= main_area_min)
        if main_area_max:
            query = query.filter(self.model.main_building_area <= main_area_max)

        if building_types:
            query = query.filter(self.model.building_type.in_(building_types))

        if main_usages:
            query = query.filter(self.model.main_use.in_(main_usages))

        if urban_land_uses:
            query = query.filter(self.model.urban_land_use_type.in_(urban_land_uses))

        if has_elevator is not None:
            query = query.filter(self.model.has_elevator == has_elevator)

        if has_management is not None:
            query = query.filter(self.model.has_management == has_management)

        if has_note is not None:
            if has_note:
                query = query.filter(self.model.remarks.isnot(None))
                query = query.filter(self.model.remarks != "")
            else:
                query = query.filter(
                    (self.model.remarks.is_(None)) | (self.model.remarks == "")
                )

        if floor_min is not None:
            query = query.filter(self.model.total_floor_number >= floor_min)
        if floor_max is not None:
            query = query.filter(self.model.total_floor_number <= floor_max)

        if room_count is not None:
            query = query.filter(self.model.building_rooms == room_count)
        if living_count is not None:
            query = query.filter(self.model.building_halls == living_count)
        if bathroom_count is not None:
            query = query.filter(self.model.building_bathrooms == bathroom_count)

        order_column = getattr(self.model, order_by, self.model.transaction_date)
        if order_desc:
            query = query.order_by(order_column.desc())
        else:
            query = query.order_by(order_column.asc())

        total = query.count()

        items = query.offset(skip).limit(limit).all()

        return {
            "total": total,
            "items": items,
            "page": (skip // limit) + 1,
            "page_size": limit,
            "total_pages": (total + limit - 1) // limit,
        }
