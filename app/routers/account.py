from fastapi import APIRouter, Depends
from app.depends import get_user
from app.schemas.account import AccountWithBalance
from app.services.account import get_accounts_with_balance

account_router = APIRouter(prefix='/account',
                           tags=['Пользователь'])


@account_router.get(path='/',
                    summary='Получить информацию о счетах',
                    description='Возвращает информацию о счетах текущего пользователя')
async def handler_get_accounts_with_balance(user=Depends(get_user)) -> list[AccountWithBalance]:
    accounts = await get_accounts_with_balance(user_id=user.user_id)
    return accounts
