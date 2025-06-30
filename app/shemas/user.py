from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str = Field(title="Email пользователя")
    fullname: str = Field(title="Полное имя пользователя")


class UserCreate(UserBase):
    password: str = Field(title="Пароль пользователя")


class User(UserBase):
    user_id: int = Field(title="ID пользователя")
