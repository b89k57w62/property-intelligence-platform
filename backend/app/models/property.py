from sqlalchemy import Column, Integer, String, Numeric, Boolean, Text, Index
from app.core.database import Base


class Property(Base):
    __tablename__ = "properties"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Location Information
    city = Column(String(50), nullable=False, index=True, comment="縣市")
    district = Column(String(50), nullable=False, index=True, comment="鄉鎮市區")
    land_location = Column(Text, comment="土地位置")
    land_section = Column(String(255), comment="土地區段位置或建物區段門牌")

    # Transaction Information
    transaction_date = Column(
        String(10), nullable=False, index=True, comment="交易年月日 (ROC format)"
    )
    transaction_pen_number = Column(String(255), comment="交易筆棟數")

    # Area Information (in square meters)
    land_area_sqm = Column(Numeric(15, 2), comment="土地移轉總面積平方公尺")
    urban_land_use_type = Column(String(100), comment="都市土地使用分區")
    non_urban_land_use_type = Column(String(100), comment="非都市土地使用分區")
    non_urban_land_use_category = Column(String(100), comment="非都市土地使用編定")
    transaction_purpose = Column(String(100), comment="交易目的")

    # Building Information
    main_use = Column(String(100), comment="主要用途")
    main_building_materials = Column(String(100), comment="主要建材")
    construction_complete_date = Column(String(10), comment="建築完成年月 (ROC format)")
    building_area_sqm = Column(Numeric(15, 2), comment="建物移轉總面積平方公尺")
    building_rooms = Column(Integer, comment="建物現況格局-房")
    building_halls = Column(Integer, comment="建物現況格局-廳")
    building_bathrooms = Column(Integer, comment="建物現況格局-衛")
    building_compartments = Column(Boolean, comment="建物現況格局-隔間 (有/無)")
    has_management = Column(Boolean, comment="有無管理組織")

    # Price Information (in NTD)
    total_floor_number = Column(Integer, comment="總樓層數")
    building_floor_number = Column(String(50), comment="建物移轉層次")
    total_price_ntd = Column(Numeric(20, 2), nullable=False, comment="總價元")
    unit_price_ntd = Column(Numeric(15, 2), comment="單價元平方公尺")
    parking_area_sqm = Column(Numeric(15, 2), comment="車位移轉總面積平方公尺")
    parking_price_ntd = Column(Numeric(20, 2), comment="車位總價元")

    # Additional Information
    remarks = Column(Text, comment="備註")
    serial_number = Column(String(100), comment="編號")

    # Composite Indexes for common search patterns
    __table_args__ = (
        Index("idx_city_district", "city", "district"),
        Index("idx_transaction_date_city", "transaction_date", "city"),
        Index("idx_price_range", "total_price_ntd"),
        Index("idx_area_range", "building_area_sqm"),
    )

    def __repr__(self):
        return f"<Property(id={self.id}, city={self.city}, district={self.district}, date={self.transaction_date})>"
