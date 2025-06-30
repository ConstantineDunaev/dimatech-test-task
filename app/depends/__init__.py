from fastapi import Request
from app.shemas.user import User


async def dependency_user(request: Request) -> User:
    """Получает пользователя по email и password"""
    headers = await request.headers()
    email = headers.get('email')
    password = headers.get('password')