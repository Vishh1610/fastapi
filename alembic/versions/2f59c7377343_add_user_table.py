"""add user table

Revision ID: 2f59c7377343
Revises: 82ba9c7d8e18
Create Date: 2026-06-23 22:21:21.970954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f59c7377343'
down_revision: Union[str, Sequence[str], None] = '82ba9c7d8e18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('email', sa.String(), nullable=False, unique=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    pass


def downgrade():
    op.drop_table('users') 
    pass
