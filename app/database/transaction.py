from app.models.transaction import Transaction
from typing import List
from app.database import AsyncSessionLocal, select, insert
from datetime import datetime


async def get_transactions(user_id: int) -> List[Transaction]:
    """Возвращает транзакций пользователя"""
    smtp = select(Transaction).where(Transaction.user_id == user_id)
    async with AsyncSessionLocal() as session:
        result = await session.execute(smtp)
        return result.scalars().all()


async def create_transaction(transaction_id: str, user_id: int, account_id: int, amount: int) -> None:
    """Создает новую транзакцию"""
    smtp = insert(Transaction).values(
        transaction_id=transaction_id,
        user_id=user_id,
        account_id=account_id,
        amount=amount,
        created_at=datetime.now()
    )
    async with AsyncSessionLocal() as session:
        await session.execute(smtp)
        await session.commit()
