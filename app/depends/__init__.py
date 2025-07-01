from fastapi import Request, Header
from app.schemas.user import User
from app.services.auth import authentication_user
from app.exceptions.user import PermissionDeniedError
from app.exceptions.webhook import InvalidSingnatureError
from app.schemas.transaction import TransactionCreate
from app.config import SECRET_KEY
from app.utils import get_hash


async def get_user(email: str = Header(..., description="Email пользователя"),
                   password: str = Header(..., description="Пароль пользователя")) -> User:
    """Возвращает пользователя по email и password"""
    user = await authentication_user(email, password)
    return user


async def get_admin(email: str = Header(..., description="Email администратора"),
                    password: str = Header(..., description="Пароль администратора")) -> User:
    """Возвращает админа по email и password"""
    user = await authentication_user(email, password)
    if not user.is_admin:
        raise PermissionDeniedError()
    return user


async def check_signature(transaction_create: TransactionCreate) -> None:
    """Проверяет подпись входящего вебхука платежа"""
    account_id = transaction_create.account_id
    amount = transaction_create.amount
    amount = int(amount) if amount.is_integer() else amount
    transaction_id = transaction_create.transaction_id
    user_id = transaction_create.user_id
    transaction_string = f"{account_id}{amount}{transaction_id}{user_id}{SECRET_KEY}"
    new_signature = get_hash(transaction_string)
    print(new_signature)
    if new_signature != transaction_create.signature:
        raise InvalidSingnatureError()
