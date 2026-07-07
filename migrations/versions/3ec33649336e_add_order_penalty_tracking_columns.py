"""add order penalty tracking columns

Revision ID: 3ec33649336e
Revises: 2a2c1c1069b4
Create Date: 2026-07-07 14:55:07.680546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ec33649336e'
down_revision: Union[str, Sequence[str], None] = '2a2c1c1069b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
