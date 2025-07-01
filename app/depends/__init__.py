from fastapi import Request
from app.schemas.user import User
from app.services.auth import authentication_user
from app.exceptions.user import PermissionDeniedError
from app.exceptions.webhook import InvalidSingnatureError
from app.schemas.transaction import TransactionCreate
from app.config import SECRET_KEY
from app.utils import get_hash


async def get_user(request: Request) -> User:
    """Возвращает пользователя по email и password"""
    headers = request.headers
    email = headers.get('email')
    password = headers.get('password')
    user = await authentication_user(email, password)
    return user


async def get_admin(request: Request) -> User:
    """Возвращает админа по email и password"""
    headers = request.headers
    email = headers.get('email')
    password = headers.get('password')
    user = await authentication_user(email, password)
    if not user.is_admin:
        raise PermissionDeniedError()
    return user


async def check_signature(transaction_create: TransactionCreate) -> None:
    """Проверяет подпись входящего вебхука платежа"""
    account_id = transaction_create.account_id
    amount = transaction_create.amount
    transaction_id = transaction_create.transaction_id
    user_id = transaction_create.user_id
    transaction_string = f"{account_id}{amount}{transaction_id}{user_id}{SECRET_KEY}"
    new_signature = get_hash(transaction_string)
    if new_signature != transaction_create.signature:
        raise InvalidSingnatureError()

