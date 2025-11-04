"""Property Rental Model"""

from sqlalchemy import Column, Integer, String, Numeric, Boolean, Text
from app.core.database import Base


class PropertyRental(Base):
    """Property rental model"""

    __tablename__ = "property_rentals"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Common Fields (20) - Shared by all tables
    district = Column(String(50), nullable=False, index=True, comment="鄉鎮市區")
    transaction_target = Column(String(50), index=True, comment="交易標的")
    land_section = Column(Text, comment="土地位置建物門牌")
    urban_land_use_type = Column(String(500), comment="都市土地使用分區")
    non_urban_land_use_type = Column(String(500), comment="非都市土地使用分區")
    non_urban_land_use_category = Column(String(500), comment="非都市土地使用編定")
    building_type = Column(String(100), index=True, comment="建物型態")
    main_use = Column(String(100), comment="主要用途")
    main_building_materials = Column(String(100), comment="主要建材")
    construction_complete_date = Column(String(10), comment="建築完成年月")
    building_rooms = Column(Integer, comment="建物現況格局-房")
    building_halls = Column(Integer, comment="建物現況格局-廳")
    building_bathrooms = Column(Integer, comment="建物現況格局-衛")
    building_compartments = Column(Boolean, comment="建物現況格局-隔間")
    has_management = Column(Boolean, comment="有無管理組織")
    total_floor_number = Column(Integer, comment="總樓層數")
    unit_price_ntd = Column(Numeric(15, 2), comment="單價元平方公尺")
    parking_type = Column(String(50), comment="車位類別")
    remarks = Column(Text, comment="備註")
    serial_number = Column(String(100), comment="編號")

    # Rental-Only Fields (16) - Only for Rental
    city = Column(String(50), nullable=False, index=True, comment="縣市")
    rental_date = Column(String(10), nullable=False, index=True, comment="租賃年月日")
    rental_pen_number = Column(String(255), comment="租賃筆棟數")
    land_area_sqm = Column(Numeric(15, 2), comment="土地面積平方公尺")
    building_area_sqm = Column(Numeric(15, 2), comment="建物總面積平方公尺")
    building_floor_number = Column(String(50), comment="租賃層次")
    has_furniture = Column(Boolean, comment="有無附傢俱")
    rental_type = Column(String(50), comment="出租型態")
    has_manager = Column(Boolean, comment="有無管理員")
    rental_period = Column(String(100), comment="租賃期間")
    has_elevator = Column(Boolean, index=True, comment="有無電梯")
    equipment = Column(Text, comment="附屬設備")
    rental_service = Column(String(100), comment="租賃住宅服務")
    monthly_rent_ntd = Column(
        Numeric(15, 2), nullable=False, index=True, comment="總額元(月租金)"
    )
    parking_area_sqm = Column(Numeric(15, 2), comment="車位面積平方公尺")
    parking_rent_ntd = Column(Numeric(15, 2), comment="車位總額元")

    def __repr__(self) -> str:
        """String representation."""
        return f"<PropertyRental(id={self.id}, city={self.city}, district={self.district})>"
