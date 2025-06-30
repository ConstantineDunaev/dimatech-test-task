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
        sa.column('transaction_id', sa.Integer),
        sa.column('account_id', sa.Integer),
        sa.column('user_id', sa.Integer),
        sa.column('amount', sa.Float),
        sa.column('created_at', sa.DateTime),
    )

    op.bulk_insert(transaction_table, [
        {
            'transaction_id': 1,
            'account_id': 2,
            'user_id': 2,
            'amount': 100,
            'created_at': datetime.now()
        },
        {
            'transaction_id': 2,
            'account_id': 2,
            'user_id': 2,
            'amount': 300,
            'created_at': datetime.now()
        },
    ])


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM \"transaction\" WHERE transaction_id IN (1, 2)")
