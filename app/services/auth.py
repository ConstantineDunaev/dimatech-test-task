from app.database.user import get_user_by_email
from app.utils import verify_password
from typing import Optional
from app.models import User
from app.exceptions.user import AuthenticationError


async def authentication_user(email: str, password: str) -> Optional[User]:
    """Возвращает пользователя по логину и паролю - используется в зависимости"""
    user = await get_user_by_email(email)
    if not user:
        raise AuthenticationError
    if not verify_password(password, user.hash_password):
        raise AuthenticationError
    return user
