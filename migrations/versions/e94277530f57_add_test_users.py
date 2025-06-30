"""add test users

Revision ID: e94277530f57
Revises: c124bf2cdbb6
Create Date: 2025-06-30 17:37:36.598955
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import hashlib


def get_hash(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


# revision identifiers, used by Alembic.
revision: str = 'c124bf2cdbb6'
down_revision: Union[str, Sequence[str], None] = 'f0699bc297f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    user_table = sa.table(
        'user',
        sa.column('user_id', sa.Integer),
        sa.column('email', sa.String),
        sa.column('full_name', sa.String),
        sa.column('hash_password', sa.String),
        sa.column('is_admin', sa.Boolean),
    )

    op.bulk_insert(user_table, [
        {
            'user_id': 1,
            'email': 'admin@example.com',
            'full_name': 'Админ',
            'hash_password': get_hash('admin_password'),
            'is_admin': True
        },
        {
            'user_id': 2,
            'email': 'user1@example.com',
            'full_name': 'Обычный Пользователь №1',
            'hash_password': get_hash('user1_password'),
            'is_admin': False
        },
    ])


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM \"user\" WHERE user_id IN (1, 2)")
