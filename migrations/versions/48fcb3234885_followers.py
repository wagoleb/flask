"""followers

Revision ID: 48fcb3234885
Revises: cf34fd97d299
Create Date: 2018-02-19 20:38:28.970412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "48fcb3234885"
down_revision = "cf34fd97d299"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["followed_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["user.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###
