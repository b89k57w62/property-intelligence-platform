"""create property_presales table

Revision ID: c1173a115b8f
Revises: ca4c5cd7bdcb
Create Date: 2025-11-04 13:23:12.420301

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c1173a115b8f"
down_revision: Union[str, None] = "ca4c5cd7bdcb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "property_presales",
        # Primary Key
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        # Common Fields (20)
        sa.Column("district", sa.String(50), nullable=False, comment="鄉鎮市區"),
        sa.Column(
            "transaction_target", sa.String(50), nullable=True, comment="交易標的"
        ),
        sa.Column("land_section", sa.Text(), nullable=True, comment="土地位置建物門牌"),
        sa.Column(
            "urban_land_use_type",
            sa.String(500),
            nullable=True,
            comment="都市土地使用分區",
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
            "construction_complete_date",
            sa.String(10),
            nullable=True,
            comment="建築完成年月",
        ),
        sa.Column(
            "building_rooms", sa.Integer(), nullable=True, comment="建物現況格局-房"
        ),
        sa.Column(
            "building_halls", sa.Integer(), nullable=True, comment="建物現況格局-廳"
        ),
        sa.Column(
            "building_bathrooms", sa.Integer(), nullable=True, comment="建物現況格局-衛"
        ),
        sa.Column(
            "building_compartments",
            sa.Boolean(),
            nullable=True,
            comment="建物現況格局-隔間",
        ),
        sa.Column(
            "has_management", sa.Boolean(), nullable=True, comment="有無管理組織"
        ),
        sa.Column(
            "total_floor_number", sa.Integer(), nullable=True, comment="總樓層數"
        ),
        sa.Column(
            "unit_price_ntd", sa.Numeric(15, 2), nullable=True, comment="單價元平方公尺"
        ),
        sa.Column("parking_type", sa.String(50), nullable=True, comment="車位類別"),
        sa.Column("remarks", sa.Text(), nullable=True, comment="備註"),
        sa.Column("serial_number", sa.String(100), nullable=True, comment="編號"),
        # Transaction & Pre-sale Shared Fields (8)
        sa.Column(
            "transaction_date", sa.String(10), nullable=False, comment="交易年月日"
        ),
        sa.Column(
            "transaction_pen_number",
            sa.String(255),
            nullable=True,
            comment="交易筆棟數",
        ),
        sa.Column(
            "land_area_sqm",
            sa.Numeric(15, 2),
            nullable=True,
            comment="土地移轉總面積平方公尺",
        ),
        sa.Column(
            "building_area_sqm",
            sa.Numeric(15, 2),
            nullable=True,
            comment="建物移轉總面積平方公尺",
        ),
        sa.Column(
            "building_floor_number",
            sa.String(50),
            nullable=True,
            comment="建物移轉層次",
        ),
        sa.Column(
            "total_price_ntd", sa.Numeric(20, 2), nullable=False, comment="總價元"
        ),
        sa.Column(
            "parking_area_sqm",
            sa.Numeric(15, 2),
            nullable=True,
            comment="車位移轉總面積平方公尺",
        ),
        sa.Column(
            "parking_price_ntd", sa.Numeric(20, 2), nullable=True, comment="車位總價元"
        ),
        # Pre-sale-Only Fields (4)
        sa.Column("city", sa.String(50), nullable=False, comment="縣市"),
        sa.Column("project_name", sa.String(200), nullable=True, comment="建案名稱"),
        sa.Column("building_number", sa.String(100), nullable=True, comment="棟及號"),
        sa.Column(
            "termination_status", sa.String(50), nullable=True, comment="解約情形"
        ),
        # Constraints
        sa.PrimaryKeyConstraint("id"),
    )

    # Create indexes
    op.create_index("idx_presale_city", "property_presales", ["city"])
    op.create_index("idx_presale_district", "property_presales", ["district"])
    op.create_index("idx_presale_date", "property_presales", ["transaction_date"])
    op.create_index("idx_presale_building_type", "property_presales", ["building_type"])
    op.create_index("idx_presale_price", "property_presales", ["total_price_ntd"])
    op.create_index("idx_presale_project", "property_presales", ["project_name"])
    op.create_index(
        "idx_presale_city_district", "property_presales", ["city", "district"]
    )


def downgrade() -> None:
    # Drop indexes first
    op.drop_index("idx_presale_city_district", table_name="property_presales")
    op.drop_index("idx_presale_project", table_name="property_presales")
    op.drop_index("idx_presale_price", table_name="property_presales")
    op.drop_index("idx_presale_building_type", table_name="property_presales")
    op.drop_index("idx_presale_date", table_name="property_presales")
    op.drop_index("idx_presale_district", table_name="property_presales")
    op.drop_index("idx_presale_city", table_name="property_presales")

    # Drop table
    op.drop_table("property_presales")
