from app.models.account import Account
from typing import List
from app.database import AsyncSessionLocal, select, text, Row


async def get_accounts_with_balance(user_id: int) -> List[Row]:
    """Возвращает список счетов с балансами"""
    sql = text("""
    SELECT account_id, name, COALESCE(sum_amount, 0) AS balance
    FROM account a 
    LEFT JOIN (
        SELECT account_id, SUM(amount) AS sum_amount
        FROM "transaction"
        GROUP BY account_id
    ) t USING (account_id)
    WHERE user_id = :user_id
    """)

    async with AsyncSessionLocal() as session:
        result = await session.execute(sql, {"user_id": user_id})
        return result.fetchall()
