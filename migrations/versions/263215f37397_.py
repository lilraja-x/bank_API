"""empty message

Revision ID: 263215f37397
Revises: 
Create Date: 2023-05-25 17:11:06.060189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '263215f37397'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_number', sa.String(length=20), nullable=True),
    sa.Column('account_title', sa.String(length=100), nullable=True),
    sa.Column('account_type', sa.String(length=100), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_number')
    )
    op.create_table('Customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_number', sa.String(length=20), nullable=False),
    sa.Column('account_title', sa.String(length=100), nullable=False),
    sa.Column('account_type', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Customers')
    op.drop_table('Accounts')
    # ### end Alembic commands ###
