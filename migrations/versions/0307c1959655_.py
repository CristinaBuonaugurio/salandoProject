"""empty message

Revision ID: 0307c1959655
Revises: 8532569330e8
Create Date: 2020-11-16 21:39:47.132850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0307c1959655'
down_revision = '8532569330e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)

    op.execute('UPDATE product SET quantity=1 WHERE quantity IS NULL;')
    
    op.alter_column('product', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
