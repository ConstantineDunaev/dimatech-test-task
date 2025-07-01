from pydantic import BaseModel, Field


class Transaction(BaseModel):
    transaction_id: str = Field(title='ID платежа')
    user_id: int = Field(title='ID пользователя')
    account_id: int = Field(title='ID счета')
    amount: float = Field(title='Сумма платежа')

    class Config:
        from_attributes = True


class TransactionCreate(Transaction):
    signature: str = Field(title='Подпись платежа')
