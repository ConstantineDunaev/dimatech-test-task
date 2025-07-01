from fastapi import APIRouter, Depends, Response, status
from app.depends import get_admin
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user import get_users, create_user, update_user, delete_user

user_router = APIRouter(prefix='/user',
                        dependencies=[Depends(get_admin)],
                        tags=['Администратор'])


@user_router.get(path='/',
                 summary='Получить список пользователей',
                 description='Возвращает список пользователей с их счетами и балансами')
async def handler_get_users() -> list[User]:
    """Возвращает список пользователей с их счетами и балансами"""
    users = await get_users()
    return users


@user_router.post(path='/',
                  summary='Создать нового пользователя',
                  description='Создание нового пользователя.'
                  )
async def handler_create_user(user_create: UserCreate) -> User:
    """Создает нового пользователя"""
    user = await create_user(user_create)
    return user


@user_router.put(path='/{user_id}',
                 summary='Обновить пользователя.',
                 description='Обновление данных существующего пользователя.'
                 )
async def handler_update_user(user_id: int, user_update: UserUpdate) -> User:
    """Обновляет пользователя"""
    user = await update_user(user_id, user_update)
    return user


@user_router.delete(path='/{user_id}',
                    status_code=status.HTTP_204_NO_CONTENT,
                    summary='Удалить пользователя',
                    description='Удаление пользователя.'
                    )
async def handler_delete_user(user_id: int):
    """Удаляет пользователя"""
    await delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


