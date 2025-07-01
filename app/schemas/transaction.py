from pydantic import BaseModel


class Transaction(BaseModel):
    transaction_id: str
    user_id: int
    account_id: int
    amount: float

    class Config:
        from_attributes = True


class TransactionCreate(Transaction):
    signature: str
