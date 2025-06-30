from fastapi import Request
from app.schemas.user import User
from app.services.user import authentication_user
from app.exceptions.user import PermissionDenied


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
        raise PermissionDenied()
    return user
