from fastapi import Request
from app.schemas.user import User
from app.services.user import authentication_user


async def get_user(request: Request) -> User:
    """Возвращает пользователя по email и password"""
    headers = request.headers
    email = headers.get('email')
    password = headers.get('password')
    user = await authentication_user(email, password)
    return user
