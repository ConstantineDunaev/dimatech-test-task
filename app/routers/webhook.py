from fastapi import APIRouter, Depends
from app.schemas.transaction import TransactionCreate
from app.depends import check_signature

webhook_router = APIRouter(prefix='/webhook')


@webhook_router.post(path='/')
async def create_transaction(transaction_create: TransactionCreate, _=Depends(check_signature)):
    """Обрабатывает входящий вебхук, создает новую транзакцию"""
    print(transaction_create)
