from fastapi import APIRouter

user_router = APIRouter(prefix='/user')


@user_router.get(path='/')
async def handler_get():
    pass
