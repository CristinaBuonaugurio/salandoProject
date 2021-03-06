"""empty message

Revision ID: 634681995c47
Revises: 65848198e97f
Create Date: 2020-11-20 17:49:37.169196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '634681995c47'
down_revision = '65848198e97f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('admin', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
