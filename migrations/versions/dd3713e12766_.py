"""empty message

Revision ID: dd3713e12766
Revises: 7e0667407ead
Create Date: 2018-12-12 21:33:38.597781

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd3713e12766'
down_revision = '7e0667407ead'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('banks', 'currency',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=8),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('banks', 'currency',
               existing_type=sa.String(length=8),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
    # ### end Alembic commands ###
