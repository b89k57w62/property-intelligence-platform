"""drop legacy properties table

Revision ID: 9a5dea43f51d
Revises: 15b38d40ecb7
Create Date: 2025-11-04 05:48:44.690979

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9a5dea43f51d"
down_revision: Union[str, None] = "15b38d40ecb7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Drop legacy properties table."""
    op.drop_table("properties")


def downgrade() -> None:
    """Note: Downgrade not implemented - would lose data."""
    pass
