"""add content column to posts table

Revision ID: 82ba9c7d8e18
Revises: bc1e22e64a06
Create Date: 2026-06-23 22:17:02.551657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82ba9c7d8e18'
down_revision: Union[str, Sequence[str], None] = 'bc1e22e64a06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
