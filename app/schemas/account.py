from pydantic import BaseModel, Field


class AccountCreate(BaseModel):
    user_id: int = Field(title="Идентификатор пользователя-владельца счета")
    name: str = Field(title="Имя счета")


class Account(AccountCreate):
    account_id: int = Field(title="Идентификатор счета")


class AccountWithBalance(BaseModel):
    name: str = Field(title="Имя счета")
    account_id: int = Field(title="Идентификатор счета")
    balance: float = Field(title="Баланс счета")
