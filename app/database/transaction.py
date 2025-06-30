from app.models.transaction import Transaction
from typing import List
from app.database import AsyncSessionLocal, select


async def get_transactions(user_id: int) -> List[Transaction]:
    """Возвращает транзакций пользователя"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Transaction).where(Transaction.user_id == user_id)
        )
        return result.scalars().all()

