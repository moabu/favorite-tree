"""create_tree_table

Revision ID: 9b26157970d9
Revises: 
Create Date: 2022-08-03 23:50:29.446243

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9b26157970d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tree',
        sa.Column('uid', sa.String(length=255),
                  nullable=False),
        sa.Column('name', sa.String(length=255),
                  nullable=False),
        sa.Column('favorite', sa.String(length=255),
                  nullable=False),
        sa.PrimaryKeyConstraint('uid'),
        sa.UniqueConstraint('favorite'),
        sa.UniqueConstraint('uid')
    )


def downgrade():
    op.drop_table('tree')
