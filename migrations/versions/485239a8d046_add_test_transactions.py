"""add test transactions

Revision ID: 485239a8d046
Revises: 053a3cde9e43
Create Date: 2025-06-30 17:52:26.094569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '485239a8d046'
down_revision: Union[str, Sequence[str], None] = '053a3cde9e43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    transaction_table = sa.table(
        'transaction',
        sa.column('transaction_id', sa.String),
        sa.column('account_id', sa.Integer),
        sa.column('user_id', sa.Integer),
        sa.column('amount', sa.Float),
        sa.column('created_at', sa.DateTime),
    )

    op.bulk_insert(transaction_table, [
        {
            'transaction_id': 'e4a1c3f2-7d9b-4f6a-9d8c-3b2e5f0a7d91',
            'account_id': 2,
            'user_id': 2,
            'amount': 100,
            'created_at': datetime.now()
        },
        {
            'transaction_id': '59f8b0c4-2a47-4d53-bda7-1e9e6c8f4b13',
            'account_id': 2,
            'user_id': 2,
            'amount': 300,
            'created_at': datetime.now()
        },
    ])


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM \"transaction\" WHERE "
               "transaction_id IN ('e4a1c3f2-7d9b-4f6a-9d8c-3b2e5f0a7d91','59f8b0c4-2a47-4d53-bda7-1e9e6c8f4b13')")
