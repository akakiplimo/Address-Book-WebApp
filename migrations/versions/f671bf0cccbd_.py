"""empty message

Revision ID: f671bf0cccbd
Revises: 
Create Date: 2022-02-21 12:22:37.415109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f671bf0cccbd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('contacts', 'address',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'address',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
