from fastapi import APIRouter, Request, Depends
from app.depends import get_user
from app.schemas.transaction import Transaction
from app.services.transaction import get_transactions

transaction_router = APIRouter(prefix='/transaction')


@transaction_router.get(path='/')
async def handler_get_transactions(_: Request, user=Depends(get_user)) -> list[Transaction]:
    transactions = await get_transactions(user.user_id)
    return transactions
