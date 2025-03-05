"""Populate users

Revision ID: 1ddaa1d3a0b7
Revises: 43aaac844962
Create Date: 2023-05-05 16:50:12.519345

"""
import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "1ddaa1d3a0b7"
down_revision = "43aaac844962"
branch_labels = None
depends_on = None


def upgrade() -> None:
    users = [
        {
            "id": 1,
            "email": "admin@beon.tech",
            "password": "admin123",
            "first_name": "John",
            "last_name": "Doe",
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        },
        {
            "id": 2,
            "email": "user@beon.tech",
            "password": "user123",
            "first_name": "Jane",
            "last_name": "Doe",
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        },
        {
            "id": 3,
            "email": "jack@yahoohoo.com",
            "password": "jack123",
            "first_name": "Jack",
            "last_name": "Sparrow",
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        },
    ]
    op.bulk_insert(
        sa.table(
            "users",
            sa.column("id", sa.Integer),
            sa.column("email", sa.String),
            sa.column("password", sa.String),
            sa.column("first_name", sa.String),
            sa.column("last_name", sa.String),
            sa.column("created_at", sa.DateTime),
            sa.column("updated_at", sa.DateTime),
        ),
        users,
    )


def downgrade() -> None:
    op.execute("DELETE FROM users")
