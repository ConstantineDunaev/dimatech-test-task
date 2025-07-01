from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str = Field(title="Email пользователя", min_length=1)
    full_name: str = Field(title="Полное имя пользователя", min_length=1)


class UserCreate(UserBase):
    password: str = Field(title="Пароль пользователя", min_length=1)


class User(UserBase):
    user_id: int = Field(title="ID пользователя")

    class Config:
        from_attributes = True

