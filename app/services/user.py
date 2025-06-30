from app.schemas.user import User
from app.database import user


async def get_users() -> list[User]:
    """Возвращает список всех пользователей"""
    users = await user.get_users()
    return [User.from_orm(item) for item in users]
