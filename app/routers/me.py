from fastapi import APIRouter, Depends
from app.depends import get_user
from app.schemas.user import User

me_router = APIRouter(prefix='/me',
                      tags=['Пользователь', 'Администратор'])


@me_router.get(path='/',
               summary='Получить данные текущего пользователя',
               description='Возвращает информацию о текущем пользователе')
async def handler_get_me(user=Depends(get_user)) -> User:
    """Возвращает информацию о текущем пользователе"""
    return User.from_orm(user)
