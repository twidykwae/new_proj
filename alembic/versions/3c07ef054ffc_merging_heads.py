"""merging heads

Revision ID: 3c07ef054ffc
Revises: 1373a17ac3c0, acdfdf0c2a76
Create Date: 2025-11-07 12:26:55.480315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3c07ef054ffc'
down_revision: Union[str, Sequence[str], None] = ('1373a17ac3c0', 'acdfdf0c2a76')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
