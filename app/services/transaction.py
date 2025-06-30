from app.database import transaction
from app.schemas.transaction import Transaction


async def get_transactions(user_id: int) -> list[Transaction]:
    """Возвращает список моделей Transaction"""
    transactions = await transaction.get_transactions(user_id)
    print(transactions)
    return [Transaction.from_orm(item) for item in transactions]
