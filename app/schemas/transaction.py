from pydantic import BaseModel


class Transaction(BaseModel):
    transaction_id: str
    user_id: int
    account_id: int
    amound: float


class TransactionCreate(Transaction):
    signature: str
