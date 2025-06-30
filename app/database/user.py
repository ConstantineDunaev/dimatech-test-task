from app.models.user import User
from typing import Optional
from app.database import AsyncSessionLocal, select


async def get_user_by_email(email: str) -> Optional[User]:
    """Возвращает пользователя по email"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()


async def get_users() -> list[User]:
    """Возвращает всех пользователей"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.is_(False))
        )
        return result.scalars().all()
