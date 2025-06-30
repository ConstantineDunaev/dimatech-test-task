from fastapi import APIRouter, Request, Depends
from app.depends import get_user
from app.schemas.user import User

user_router = APIRouter(prefix='/user')


@user_router.get(path='/')
async def handler_get_users():
    pass


@user_router.get(path='/me')
async def handler_get_me(_: Request, user=Depends(get_user)) -> User:
    return User(user_id=user.user_id,
                email=user.email,
                full_name=user.full_name)
