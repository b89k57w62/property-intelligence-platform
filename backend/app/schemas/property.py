"""Property schemas for API request/response models."""

from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class PropertyResponse(BaseModel):
    """
    Property Data Transfer Object for API responses.

    Maps ORM Property model to API response format.
    All fields match the database schema.
    """

    # Primary Key
    id: int

    # Location Information
    city: str
    district: str
    land_location: Optional[str] = None
    land_section: Optional[str] = None

    # Transaction Information
    transaction_date: str
    transaction_pen_number: Optional[str] = None
    transaction_target: Optional[str] = None

    # Area Information (in square meters)
    land_area_sqm: Optional[Decimal] = None
    urban_land_use_type: Optional[str] = None
    non_urban_land_use_type: Optional[str] = None
    non_urban_land_use_category: Optional[str] = None
    transaction_purpose: Optional[str] = None

    # Building Information
    building_type: Optional[str] = None
    main_use: Optional[str] = None
    main_building_materials: Optional[str] = None
    construction_complete_date: Optional[str] = None
    building_area_sqm: Optional[Decimal] = None
    main_building_area: Optional[Decimal] = None
    auxiliary_building_area: Optional[Decimal] = None
    balcony_area: Optional[Decimal] = None
    building_rooms: Optional[int] = None
    building_halls: Optional[int] = None
    building_bathrooms: Optional[int] = None
    building_compartments: Optional[bool] = None
    has_management: Optional[bool] = None
    has_elevator: Optional[bool] = None

    # Price Information (in NTD)
    total_floor_number: Optional[int] = None
    building_floor_number: Optional[str] = None
    total_price_ntd: Decimal
    unit_price_ntd: Optional[Decimal] = None
    parking_type: Optional[str] = None
    parking_area_sqm: Optional[Decimal] = None
    parking_price_ntd: Optional[Decimal] = None

    # Additional Information
    remarks: Optional[str] = None
    serial_number: Optional[str] = None

    # Pydantic v2 configuration
    model_config = ConfigDict(from_attributes=True)


class PropertySearchResponse(BaseModel):
    """
    Paginated search results response.

    Contains list of properties and pagination metadata.
    """

    total: int
    items: List[PropertyResponse]
    page: int
    page_size: int
    total_pages: int
