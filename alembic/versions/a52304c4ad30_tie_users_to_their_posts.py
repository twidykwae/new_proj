"""tie users to their posts

Revision ID: a52304c4ad30
Revises: 377230e30d1e
Create Date: 2025-12-26 13:28:26.349941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a52304c4ad30'
down_revision: Union[str, Sequence[str], None] = '377230e30d1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    with op.batch_alter_table("lostandfounditem", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("user_id", sa.Integer(), nullable=True)
        )
        batch_op.create_foreign_key(
            "fk_lostandfounditem_user",
            "userbase",
            ["user_id"],
            ["id"]
        )

    with op.batch_alter_table("prayerrequest", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("user_id", sa.Integer(), nullable=True)
        )
        batch_op.create_foreign_key(
            "fk_prayerrequest_user",
            "userbase",
            ["user_id"],
            ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("prayerrequest", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_prayerrequest_user",
            type_="foreignkey"
        )
        batch_op.drop_column("user_id")

    with op.batch_alter_table("lostandfounditem", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_lostandfounditem_user",
            type_="foreignkey"
        )
        batch_op.drop_column("user_id")

