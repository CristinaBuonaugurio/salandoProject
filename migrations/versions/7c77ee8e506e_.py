"""empty message

Revision ID: 7c77ee8e506e
Revises: ff1686b7147f
Create Date: 2020-11-20 19:06:19.998251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c77ee8e506e'
down_revision = 'ff1686b7147f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('password', sa.LargeBinary(), nullable=False))
    op.add_column('users', sa.Column('password', sa.LargeBinary(length=60), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('admin', 'password')
    # ### end Alembic commands ###
