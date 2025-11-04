"""Property transaction schemas for API request/response models"""

from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class PropertyTransactionResponse(BaseModel):
    """DTO for property transaction API responses."""

    id: int

    # Common fields
    district: str
    transaction_target: Optional[str] = None
    land_section: Optional[str] = None
    urban_land_use_type: Optional[str] = None
    non_urban_land_use_type: Optional[str] = None
    non_urban_land_use_category: Optional[str] = None
    building_type: Optional[str] = None
    main_use: Optional[str] = None
    main_building_materials: Optional[str] = None
    construction_complete_date: Optional[str] = None
    building_rooms: Optional[int] = None
    building_halls: Optional[int] = None
    building_bathrooms: Optional[int] = None
    building_compartments: Optional[bool] = None
    has_management: Optional[bool] = None
    total_floor_number: Optional[int] = None
    unit_price_ntd: Optional[Decimal] = None
    parking_type: Optional[str] = None
    remarks: Optional[str] = None
    serial_number: Optional[str] = None

    # Transaction shared fields
    transaction_date: str
    transaction_pen_number: Optional[str] = None
    land_area_sqm: Optional[Decimal] = None
    building_area_sqm: Optional[Decimal] = None
    building_floor_number: Optional[str] = None
    total_price_ntd: Decimal
    parking_area_sqm: Optional[Decimal] = None
    parking_price_ntd: Optional[Decimal] = None

    # Transaction-only fields
    city: str
    main_building_area: Optional[Decimal] = None
    auxiliary_building_area: Optional[Decimal] = None
    balcony_area: Optional[Decimal] = None
    has_elevator: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class PropertyTransactionSearchResponse(BaseModel):
    """Paginated search results response."""

    total: int
    items: List[PropertyTransactionResponse]
    page: int
    page_size: int
    total_pages: int
