"""users table

Revision ID: a1141a03eee9
Revises: e9f7b4333eeb
Create Date: 2022-05-29 19:48:07.455367

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a1141a03eee9'
down_revision = 'e9f7b4333eeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('main_page')
    op.drop_table('roles_users')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=40), nullable=True),
    sa.Column('email', sa.VARCHAR(length=40), nullable=True),
    sa.Column('message', sa.VARCHAR(length=350), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('main_page',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('biography_title', sa.VARCHAR(length=200), nullable=True),
    sa.Column('education', sa.VARCHAR(length=350), nullable=True),
    sa.Column('curriculum_vitae', sa.VARCHAR(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
