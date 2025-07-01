from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    email: str = Field(title="Email пользователя", min_length=5)
    full_name: str = Field(title="Полное имя пользователя", min_length=5)


class UserCreate(UserBase):
    password: str = Field(title="Пароль пользователя", min_length=5)


class UserUpdate(BaseModel):
    email: Optional[str] = Field(title="Email пользователя", min_length=5, default=None)
    password: Optional[str] = Field(title="Пароль пользователя", min_length=5, default=None)
    full_name: Optional[str] = Field(title="Полное имя пользователя", min_length=5, default=None)


class User(UserBase):
    user_id: int = Field(title="ID пользователя")

    class Config:
        from_attributes = True
