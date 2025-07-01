from fastapi import APIRouter, Request, Depends, Response, status
from app.depends import get_admin
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user import get_users, create_user, update_user, delete_user

user_router = APIRouter(prefix='/user')


@user_router.get(path='/')
async def handler_get_users(_: Request, admin=Depends(get_admin)) -> list[User]:
    """Возвращает список пользователей"""
    users = await get_users()
    return users


@user_router.post(path='/')
async def handler_create_user(user_create: UserCreate, admin=Depends(get_admin)) -> User:
    """Создает нового пользователя"""
    user = await create_user(user_create)
    return user


@user_router.put(path='/{user_id}')
async def handler_update_user(user_id: int, user_update: UserUpdate, admin=Depends(get_admin)) -> User:
    """Обновляет пользователя"""
    user = await update_user(user_id, user_update)
    return user


@user_router.delete(path='/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def handler_delete_user(user_id: int):
    """Удаляет пользователя"""
    await delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
