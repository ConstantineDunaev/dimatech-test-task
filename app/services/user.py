from app.schemas.user import User, UserCreate
from app.database import user as user_db
from app.utils import get_hash
from sqlalchemy.exc import IntegrityError
from app.exceptions.user import EmailAlreadyExistsError


async def get_users() -> list[User]:
    """Возвращает список всех пользователей"""
    users = await user_db.get_users()
    return [User.from_orm(item) for item in users]


async def create_user(user_create: UserCreate) -> User:
    """Создает и возвращает нового пользователя"""
    email = user_create.email
    full_name = user_create.full_name
    hash_password = get_hash(user_create.password)
    try:
        user = await user_db.create_user(email, full_name, hash_password)
    except IntegrityError as e:
        raise EmailAlreadyExistsError(email)
    return User.from_orm(user)
