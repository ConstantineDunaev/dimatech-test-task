from sqlalchemy.orm import Session
from app.database.user import get_user_by_email
from app.utils import verify_password
from typing import Optional
from app.shemas.user import User


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """Возвращает пользователя по логину и паролю"""
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hash_password):
        return None
    return user


