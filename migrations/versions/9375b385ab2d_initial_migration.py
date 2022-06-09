"""Initial Migration

Revision ID: 9375b385ab2d
Revises: cdbbbd0be8ad
Create Date: 2022-02-28 23:24:46.253865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9375b385ab2d'
down_revision = 'cdbbbd0be8ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###