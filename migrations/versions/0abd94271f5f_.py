"""empty message

Revision ID: 0abd94271f5f
Revises: dd780c7419e3
Create Date: 2020-11-20 17:39:15.246638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0abd94271f5f'
down_revision = 'dd780c7419e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin', 'password')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=10), autoincrement=False, nullable=False))
    op.add_column('admin', sa.Column('password', sa.VARCHAR(length=10), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
