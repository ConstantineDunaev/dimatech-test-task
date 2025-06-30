from fastapi import APIRouter, Request, Depends
from app.depends import get_user, get_admin
from app.schemas.user import User

user_router = APIRouter(prefix='/user')


@user_router.get(path='/')
async def handler_get_users(_: Request, admin=Depends(get_admin)) -> list[User]:
    pass
