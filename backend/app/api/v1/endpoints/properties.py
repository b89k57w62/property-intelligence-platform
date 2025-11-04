"""Property API endpoints."""

from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.property_service import PropertyService
from app.schemas.property import PropertyResponse, PropertySearchResponse

router = APIRouter()


@router.get("/{property_id}", response_model=PropertyResponse)
def get_property(property_id: int, db: Session = Depends(get_db)):
    """
    Get single property by ID

    Args:
        property_id: Property ID

    Returns:
        PropertyResponse: Property details

    Raises:
        404: Property not found
    """
    service = PropertyService(db)
    result = service.get_by_id(property_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Property with ID {property_id} not found",
        )

    return result


@router.get("/", response_model=PropertySearchResponse)
def search_properties(
    # Location filters
    city: Optional[str] = Query(None, description="City name (e.g., 台北市)"),
    district: Optional[str] = Query(None, description="District name (e.g., 大安區)"),
    address_keyword: Optional[str] = Query(
        None, description="Address keyword for fuzzy search"
    ),
    # Transaction filters
    transaction_targets: Optional[List[str]] = Query(
        None, description="Transaction targets (房地/建物/土地/車位)"
    ),
    # Date range (ROC format)
    date_from: Optional[str] = Query(
        None,
        description="Start date in ROC format (中華民國): YYYMMDD or YYMMDD (e.g., 1130101 = 2024-01-01)",
        example="1130101",
    ),
    date_to: Optional[str] = Query(
        None,
        description="End date in ROC format (中華民國): YYYMMDD or YYMMDD (e.g., 1141231 = 2025-12-31)",
        example="1141231",
    ),
    # Price range
    price_min: Optional[int] = Query(None, description="Minimum unit price (NTD/sqm)"),
    price_max: Optional[int] = Query(None, description="Maximum unit price (NTD/sqm)"),
    total_price_min: Optional[int] = Query(
        None, description="Minimum total price (NTD)"
    ),
    total_price_max: Optional[int] = Query(
        None, description="Maximum total price (NTD)"
    ),
    # Area range
    area_min: Optional[float] = Query(None, description="Minimum building area (sqm)"),
    area_max: Optional[float] = Query(None, description="Maximum building area (sqm)"),
    main_area_min: Optional[float] = Query(
        None, description="Minimum main building area (sqm)"
    ),
    main_area_max: Optional[float] = Query(
        None, description="Maximum main building area (sqm)"
    ),
    # Building filters
    building_types: Optional[List[str]] = Query(None, description="Building types"),
    main_usages: Optional[List[str]] = Query(None, description="Main building usages"),
    urban_land_uses: Optional[List[str]] = Query(
        None, description="Urban land use types"
    ),
    # Special conditions
    has_elevator: Optional[bool] = Query(None, description="Has elevator"),
    has_management: Optional[bool] = Query(None, description="Has management"),
    # Floor range
    floor_min: Optional[int] = Query(None, description="Minimum floor"),
    floor_max: Optional[int] = Query(None, description="Maximum floor"),
    # Layout
    room_count: Optional[int] = Query(None, description="Number of rooms"),
    living_count: Optional[int] = Query(None, description="Number of living rooms"),
    bathroom_count: Optional[int] = Query(None, description="Number of bathrooms"),
    # Pagination
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Maximum records to return"),
    # Sorting
    order_by: str = Query("transaction_date", description="Field to sort by"),
    order_desc: bool = Query(True, description="Sort in descending order"),
    db: Session = Depends(get_db),
):
    """
    Search properties with multiple filters

    Returns:
        PropertySearchResponse: Paginated search results with metadata
    """
    service = PropertyService(db)

    # Build filters dict
    filters = {}
    if city:
        filters["city"] = city
    if district:
        filters["district"] = district
    if address_keyword:
        filters["address_keyword"] = address_keyword
    if transaction_targets:
        filters["transaction_targets"] = transaction_targets
    if date_from:
        filters["date_from"] = date_from
    if date_to:
        filters["date_to"] = date_to
    if price_min is not None:
        filters["price_min"] = price_min
    if price_max is not None:
        filters["price_max"] = price_max
    if total_price_min is not None:
        filters["total_price_min"] = total_price_min
    if total_price_max is not None:
        filters["total_price_max"] = total_price_max
    if area_min is not None:
        filters["area_min"] = area_min
    if area_max is not None:
        filters["area_max"] = area_max
    if main_area_min is not None:
        filters["main_area_min"] = main_area_min
    if main_area_max is not None:
        filters["main_area_max"] = main_area_max
    if building_types:
        filters["building_types"] = building_types
    if main_usages:
        filters["main_usages"] = main_usages
    if urban_land_uses:
        filters["urban_land_uses"] = urban_land_uses
    if has_elevator is not None:
        filters["has_elevator"] = has_elevator
    if has_management is not None:
        filters["has_management"] = has_management
    if floor_min is not None:
        filters["floor_min"] = floor_min
    if floor_max is not None:
        filters["floor_max"] = floor_max
    if room_count is not None:
        filters["room_count"] = room_count
    if living_count is not None:
        filters["living_count"] = living_count
    if bathroom_count is not None:
        filters["bathroom_count"] = bathroom_count
    if order_by:
        filters["order_by"] = order_by
    if order_desc is not None:
        filters["order_desc"] = order_desc

    return service.search_properties(filters=filters, skip=skip, limit=limit)
