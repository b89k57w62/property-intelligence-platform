"""Increase column lengths for long text fields

Revision ID: 3b45be381d0e
Revises: 8bbfac4cf5da
Create Date: 2025-11-03 06:46:23.012997

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3b45be381d0e"
down_revision: Union[str, None] = "8bbfac4cf5da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Increase VARCHAR lengths for fields that may contain long text
    op.alter_column(
        "properties",
        "urban_land_use_type",
        existing_type=sa.String(length=100),
        type_=sa.String(length=500),
        existing_nullable=True,
    )

    op.alter_column(
        "properties",
        "non_urban_land_use_type",
        existing_type=sa.String(length=100),
        type_=sa.String(length=500),
        existing_nullable=True,
    )

    op.alter_column(
        "properties",
        "non_urban_land_use_category",
        existing_type=sa.String(length=100),
        type_=sa.String(length=500),
        existing_nullable=True,
    )

    op.alter_column(
        "properties",
        "land_section",
        existing_type=sa.String(length=255),
        type_=sa.String(length=500),
        existing_nullable=True,
    )


def downgrade() -> None:
    # Revert to original lengths
    op.alter_column(
        "properties",
        "land_section",
        existing_type=sa.String(length=500),
        type_=sa.String(length=255),
        existing_nullable=True,
    )

    op.alter_column(
        "properties",
        "non_urban_land_use_category",
        existing_type=sa.String(length=500),
        type_=sa.String(length=100),
        existing_nullable=True,
    )

    op.alter_column(
        "properties",
        "non_urban_land_use_type",
        existing_type=sa.String(length=500),
        type_=sa.String(length=100),
        existing_nullable=True,
    )

    op.alter_column(
        "properties",
        "urban_land_use_type",
        existing_type=sa.String(length=500),
        type_=sa.String(length=100),
        existing_nullable=True,
    )
