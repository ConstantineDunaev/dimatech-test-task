from app.schemas.user import User, UserCreate, UserUpdate
from app.database import user as user_db
from app.utils import get_hash
from sqlalchemy.exc import NoResultFound, IntegrityError
from app.exceptions.user import EmailAlreadyExistsError, UserNotFoundError, UserHasAccountsError


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
    except IntegrityError:
        raise EmailAlreadyExistsError(email)
    return User.from_orm(user)


async def update_user(user_id: int, user_update: UserUpdate) -> User:
    """Обновляет данные пользователя"""
    email = user_update.email
    full_name = user_update.full_name
    hash_password = get_hash(user_update.password)
    try:
        user = await user_db.update_user(user_id, email, full_name, hash_password)
    except IntegrityError:
        raise EmailAlreadyExistsError(email)
    except NoResultFound:
        raise UserNotFoundError(user_id)
    return User.from_orm(user)


async def delete_user(user_id: int) -> None:
    """Удаляет пользователя из БД"""
    try:
        row_count = await user_db.delete_user(user_id)
        if row_count == 0:
            raise UserNotFoundError(user_id)
    except IntegrityError:
        raise UserHasAccountsError(user_id)
