"""add payout tracking to order

Revision ID: c3eb3f424560
Revises: 219db5d9acbc
Create Date: 2026-07-08 21:37:51.028818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3eb3f424560'
down_revision: Union[str, Sequence[str], None] = '219db5d9acbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
