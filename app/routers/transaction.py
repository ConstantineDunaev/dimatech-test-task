from fastapi import APIRouter, Depends
from app.depends import get_user
from app.schemas.transaction import Transaction
from app.services.transaction import get_transactions

transaction_router = APIRouter(prefix='/transaction',
                               tags=['Пользователь'])


@transaction_router.get(path='/',
                        summary='Получить информацию о транзакциях',
                        description='Возвращает инфорамцию о транзакциях текушего пользователя')
async def handler_get_transactions(user=Depends(get_user)) -> list[Transaction]:
    """Возвращает инфорамцию о транзакциях текушего пользователя"""
    transactions = await get_transactions(user.user_id)
    return transactions
