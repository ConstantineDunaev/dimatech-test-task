from app.models.user import User
from typing import Optional
from app.database import AsyncSessionLocal, select, insert


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


async def create_user(email: str, full_name: str, hash_password: str):
    """Создает пользователя"""
    async with AsyncSessionLocal() as session:
        stmt = insert(User).values(
            email=email,
            full_name=full_name,
            hash_password=hash_password
        ).returning(User)

        result = await session.execute(stmt)
        await session.commit()

        return result.scalar_one()


