from fastapi import APIRouter, Depends
from app.depends import get_user
from app.schemas.user import User

me_router = APIRouter(prefix='/me')


@me_router.get(path='/')
async def handler_get_me(user=Depends(get_user)) -> User:
    return User.from_orm(user)
