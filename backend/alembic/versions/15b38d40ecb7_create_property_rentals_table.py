"""create property_rentals table

Revision ID: 15b38d40ecb7
Revises: c1173a115b8f
Create Date: 2025-11-04 13:24:26.391157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "15b38d40ecb7"
down_revision: Union[str, None] = "c1173a115b8f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "property_rentals",
        # Primary Key
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        # Common Fields (20)
        sa.Column("district", sa.String(50), nullable=False, comment="鄉鎮市區"),
        sa.Column("transaction_target", sa.String(50), nullable=True, comment="交易標的"),
        sa.Column("land_section", sa.Text(), nullable=True, comment="土地位置建物門牌"),
        sa.Column(
            "urban_land_use_type", sa.String(500), nullable=True, comment="都市土地使用分區"
        ),
        sa.Column(
            "non_urban_land_use_type",
            sa.String(500),
            nullable=True,
            comment="非都市土地使用分區",
        ),
        sa.Column(
            "non_urban_land_use_category",
            sa.String(500),
            nullable=True,
            comment="非都市土地使用編定",
        ),
        sa.Column("building_type", sa.String(100), nullable=True, comment="建物型態"),
        sa.Column("main_use", sa.String(100), nullable=True, comment="主要用途"),
        sa.Column(
            "main_building_materials", sa.String(100), nullable=True, comment="主要建材"
        ),
        sa.Column(
            "construction_complete_date", sa.String(10), nullable=True, comment="建築完成年月"
        ),
        sa.Column("building_rooms", sa.Integer(), nullable=True, comment="建物現況格局-房"),
        sa.Column("building_halls", sa.Integer(), nullable=True, comment="建物現況格局-廳"),
        sa.Column(
            "building_bathrooms", sa.Integer(), nullable=True, comment="建物現況格局-衛"
        ),
        sa.Column(
            "building_compartments", sa.Boolean(), nullable=True, comment="建物現況格局-隔間"
        ),
        sa.Column("has_management", sa.Boolean(), nullable=True, comment="有無管理組織"),
        sa.Column("total_floor_number", sa.Integer(), nullable=True, comment="總樓層數"),
        sa.Column(
            "unit_price_ntd", sa.Numeric(15, 2), nullable=True, comment="單價元平方公尺"
        ),
        sa.Column("parking_type", sa.String(50), nullable=True, comment="車位類別"),
        sa.Column("remarks", sa.Text(), nullable=True, comment="備註"),
        sa.Column("serial_number", sa.String(100), nullable=True, comment="編號"),
        # Rental-Only Fields (16)
        sa.Column("city", sa.String(50), nullable=False, comment="縣市"),
        sa.Column("rental_date", sa.String(10), nullable=False, comment="租賃年月日"),
        sa.Column("rental_pen_number", sa.String(255), nullable=True, comment="租賃筆棟數"),
        sa.Column(
            "land_area_sqm", sa.Numeric(15, 2), nullable=True, comment="土地面積平方公尺"
        ),
        sa.Column(
            "building_area_sqm", sa.Numeric(15, 2), nullable=True, comment="建物總面積平方公尺"
        ),
        sa.Column(
            "building_floor_number", sa.String(50), nullable=True, comment="租賃層次"
        ),
        sa.Column("has_furniture", sa.Boolean(), nullable=True, comment="有無附傢俱"),
        sa.Column("rental_type", sa.String(50), nullable=True, comment="出租型態"),
        sa.Column("has_manager", sa.Boolean(), nullable=True, comment="有無管理員"),
        sa.Column("rental_period", sa.String(100), nullable=True, comment="租賃期間"),
        sa.Column("has_elevator", sa.Boolean(), nullable=True, comment="有無電梯"),
        sa.Column("equipment", sa.Text(), nullable=True, comment="附屬設備"),
        sa.Column("rental_service", sa.String(100), nullable=True, comment="租賃住宅服務"),
        sa.Column("monthly_rent_ntd", sa.Numeric(15, 2), nullable=False, comment="總額元"),
        sa.Column(
            "parking_area_sqm", sa.Numeric(15, 2), nullable=True, comment="車位面積平方公尺"
        ),
        sa.Column(
            "parking_rent_ntd", sa.Numeric(15, 2), nullable=True, comment="車位總額元"
        ),
        # Constraints
        sa.PrimaryKeyConstraint("id"),
    )

    # Create indexes
    op.create_index("idx_rental_city", "property_rentals", ["city"])
    op.create_index("idx_rental_district", "property_rentals", ["district"])
    op.create_index("idx_rental_date", "property_rentals", ["rental_date"])
    op.create_index("idx_rental_building_type", "property_rentals", ["building_type"])
    op.create_index("idx_rental_monthly_rent", "property_rentals", ["monthly_rent_ntd"])
    op.create_index("idx_rental_elevator", "property_rentals", ["has_elevator"])
    op.create_index(
        "idx_rental_city_district", "property_rentals", ["city", "district"]
    )


def downgrade() -> None:
    # Drop indexes first
    op.drop_index("idx_rental_city_district", table_name="property_rentals")
    op.drop_index("idx_rental_elevator", table_name="property_rentals")
    op.drop_index("idx_rental_monthly_rent", table_name="property_rentals")
    op.drop_index("idx_rental_building_type", table_name="property_rentals")
    op.drop_index("idx_rental_date", table_name="property_rentals")
    op.drop_index("idx_rental_district", table_name="property_rentals")
    op.drop_index("idx_rental_city", table_name="property_rentals")

    # Drop table
    op.drop_table("property_rentals")
