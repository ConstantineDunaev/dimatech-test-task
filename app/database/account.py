from app.models.account import Account
from typing import List
from app.database import AsyncSessionLocal, select


async def get_account(user_id: int) -> List[Account]:
    """Возвращает список счетов с балансами"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Account).where(Account.user_id == user_id)
        )
        return result.scalar_one_or_none()
