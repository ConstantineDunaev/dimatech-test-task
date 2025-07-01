from app.models.user import User
from typing import Optional
from app.database import AsyncSessionLocal, select, insert, update, delete


async def get_user_by_email(email: str) -> Optional[User]:
    """Возвращает пользователя по email"""
    smtp = select(User).where(User.email == email)
    async with AsyncSessionLocal() as session:
        result = await session.execute(smtp)
        return result.scalar_one_or_none()


async def get_users() -> list[User]:
    """Возвращает всех пользователей"""
    smtp = select(User)
    async with AsyncSessionLocal() as session:
        result = await session.execute(smtp)
        return result.scalars().all()


async def create_user(email: str, full_name: str, hash_password: str) -> User:
    """Создает пользователя"""
    stmt = insert(User).values(
        email=email,
        full_name=full_name,
        hash_password=hash_password
    ).returning(User)
    async with AsyncSessionLocal() as session:
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one()


async def update_user(user_id: int, email: str, full_name: str, hash_password: str) -> User:
    """Обновляет пользователя"""
    stmt = select(User).where(User.user_id == user_id)
    async with AsyncSessionLocal() as session:
        result = await session.execute(stmt)
        user = result.scalar_one()

        if email and email != user.email:
            user.email = email
        if hash_password and hash_password != user.hash_password:
            user.hash_password = hash_password
        if full_name and full_name != user.full_name:
            user.full_name = full_name

        await session.commit()
        await session.refresh(user)

        return user



async def delete_user(user_id: int) -> int:
    """Удаляет пользователя"""
    stmt = delete(User).where(User.user_id == user_id)
    async with AsyncSessionLocal() as session:
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount


async def get_user(user_id: int) -> User:
    """Возвращает пользователя"""
    stmt = select(User).where(User.user_id == user_id).where(User.is_admin.is_(False))
    async with AsyncSessionLocal() as session:
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
