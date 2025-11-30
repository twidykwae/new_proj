"""add is_admin column to users

Revision ID: ded9d6cda070
Revises: 95b409c54f99
Create Date: 2025-11-29 23:47:10.206341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ded9d6cda070'
down_revision: Union[str, Sequence[str], None] = '95b409c54f99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
