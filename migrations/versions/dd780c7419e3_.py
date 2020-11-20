"""empty message

Revision ID: dd780c7419e3
Revises: cc5f500c7315
Create Date: 2020-11-20 17:03:13.644416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd780c7419e3'
down_revision = 'cc5f500c7315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('userbuyproduct', 'methodofpayment',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('userbuyproduct', 'methodofpayment',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    # ### end Alembic commands ###
