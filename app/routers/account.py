from fastapi import APIRouter, Request, Depends
from app.depends import get_user
from app.schemas.account import AccountWithBalance
from app.services.account import get_accounts_with_balance

account_router = APIRouter(prefix='/account')


@account_router.get(path='/')
async def handler_get_accounts_with_balance(_: Request, user=Depends(get_user)) -> list[AccountWithBalance]:
    accounts = await get_accounts_with_balance(user_id=user.user_id)
    return accounts
