from app.models.transaction import Transaction
from typing import List
from app.database import AsyncSessionLocal, select, text, Row


async def get_accounts_with_balance(user_id: int) -> List[Transaction]:
    """Возвращает транзакций пользователя"""
    sql = text("""
    """)

    async with AsyncSessionLocal() as session:
        result = await session.execute(sql, {"user_id": user_id})
        return result.fetchall()
