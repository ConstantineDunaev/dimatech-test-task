"""add test accounts

Revision ID: 053a3cde9e43
Revises: c124bf2cdbb6
Create Date: 2025-06-30 17:52:14.981683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '053a3cde9e43'
down_revision: Union[str, Sequence[str], None] = 'c124bf2cdbb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""
    account_table = sa.table(
        'account',
        sa.column('account_id', sa.Integer),
        sa.column('user_id', sa.Integer),
        sa.column('name', sa.String)
    )

    op.bulk_insert(account_table, [
        {
            'account_id': 1,
            'user_id': 2,
            'name': 'Счет №1'
        },
        {
            'account_id': 2,
            'user_id': 2,
            'name': 'Счет №2'
        },
    ])


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM \"account\" WHERE account_id IN (1, 2)")