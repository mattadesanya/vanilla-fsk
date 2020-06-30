"""empty message

Revision ID: 18195a47e2ac
Revises: f52bf951262a
Create Date: 2020-06-30 23:56:40.995906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18195a47e2ac'
down_revision = 'f52bf951262a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('permissions', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('permissions', sa.Column('f_id', sa.String(length=50), nullable=False))
    op.add_column('permissions', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('permissions', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.add_column('role_permissions', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('role_permissions', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('role_permissions', sa.Column('f_id', sa.String(length=50), nullable=False))
    op.add_column('role_permissions', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('role_permissions', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.add_column('roles', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('roles', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('roles', sa.Column('f_id', sa.String(length=50), nullable=False))
    op.add_column('roles', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('roles', sa.Column('updated_by', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'updated_by')
    op.drop_column('roles', 'updated_at')
    op.drop_column('roles', 'f_id')
    op.drop_column('roles', 'created_by')
    op.drop_column('roles', 'created_at')
    op.drop_column('role_permissions', 'updated_by')
    op.drop_column('role_permissions', 'updated_at')
    op.drop_column('role_permissions', 'f_id')
    op.drop_column('role_permissions', 'created_by')
    op.drop_column('role_permissions', 'created_at')
    op.drop_column('permissions', 'updated_by')
    op.drop_column('permissions', 'updated_at')
    op.drop_column('permissions', 'f_id')
    op.drop_column('permissions', 'created_by')
    op.drop_column('permissions', 'created_at')
    # ### end Alembic commands ###