"""initiate

Revision ID: eabadc17a340
Revises: 
Create Date: 2020-05-18 16:00:34.025020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eabadc17a340'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('book')
