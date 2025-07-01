from fastapi import APIRouter, Request, Depends
from app.depends import get_admin
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user import get_users, create_user, update_user

user_router = APIRouter(prefix='/user')


@user_router.get(path='/')
async def handler_get_users(_: Request, admin=Depends(get_admin)) -> list[User]:
    users = await get_users()
    return users


@user_router.post(path='/')
async def handler_create_user(user_create: UserCreate, admin=Depends(get_admin)) -> User:
    user = await create_user(user_create)
    return user


@user_router.put(path='/{user_id}')
async def handler_update_user(user_id: int, user_update: UserUpdate, admin=Depends(get_admin)) -> User:
    user = await update_user(user_id, user_update)
    return user
