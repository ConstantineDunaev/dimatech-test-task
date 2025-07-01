from fastapi import APIRouter, Depends
from app.depends import get_user
from app.schemas.transaction import Transaction
from app.services.transaction import get_transactions

transaction_router = APIRouter(prefix='/transaction',
                               tags=['Администратор', 'Пользователь'])


@transaction_router.get(path='/',
                        summary='Получить информацию о платежах',
                        description='Возвращает инфорамцию о платежах текущего пользователя')
async def handler_get_transactions(user=Depends(get_user)) -> list[Transaction]:
    """Возвращает инфорамцию о платежах текушего пользователя"""
    transactions = await get_transactions(user.user_id)
    return transactions
