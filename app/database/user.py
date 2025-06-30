from sqlalchemy.orm import Session
from app.models.user import User
from typing import Optional


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Возвращает пользователя по email"""
    return db.query(User).filter(User.email == email).first()


