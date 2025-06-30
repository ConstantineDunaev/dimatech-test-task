from fastapi import APIRouter, Request, Depends
from app.depends import get_user
from app.schemas.user import User

me_router = APIRouter(prefix='/me')


@me_router.get(path='/me')
async def handler_get_me(_: Request, user=Depends(get_user)) -> User:
    return User.from_orm(user)
