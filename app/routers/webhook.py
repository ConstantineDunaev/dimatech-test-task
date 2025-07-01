from fastapi import APIRouter, Depends, Response, status
from app.schemas.transaction import TransactionCreate
from app.depends import check_signature
from app.services.transaction import create_transaction

webhook_router = APIRouter(prefix='/webhook',
                           dependencies=[Depends(check_signature)],
                           tags=['Входящие платежи'])


@webhook_router.post(path='/',
                     status_code=status.HTTP_204_NO_CONTENT,
                     summary='Прием webhook',
                     description='Принимает webhook от платежной системы, создает новый платеж.')
async def handler_create_transaction(transaction_create: TransactionCreate):
    """Принимает webhook от платежной системы, создает новый платеж"""
    await create_transaction(transaction_create)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
