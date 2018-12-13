"""empty message

Revision ID: e1f731146534
Revises: 8ec40471dbce
Create Date: 2018-12-12 17:52:44.613994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1f731146534'
down_revision = '8ec40471dbce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('banks', sa.Column('balance', sa.Float(), nullable=False))
    op.add_column('banks', sa.Column('currency', sa.Integer(), nullable=False))
    op.add_column('banks', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'banks', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'banks', type_='foreignkey')
    op.drop_column('banks', 'user_id')
    op.drop_column('banks', 'currency')
    op.drop_column('banks', 'balance')
    # ### end Alembic commands ###
