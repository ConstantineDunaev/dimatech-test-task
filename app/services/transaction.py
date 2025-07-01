from app.database import transaction as transaction_db
from app.database import user as user_db
from app.database import account as account_db
from app.schemas.transaction import Transaction, TransactionCreate
from app.exceptions import UserNotFoundError, AccountNotFoundError


async def get_transactions(user_id: int) -> list[Transaction]:
    """Возвращает список моделей Transaction"""
    transactions = await transaction_db.get_transactions(user_id)
    return [Transaction.from_orm(item) for item in transactions]


async def create_transaction(transaction_create: TransactionCreate) -> None:
    """Создает новую транзакцию"""
    transaction_id = transaction_create.transaction_id
    user_id = transaction_create.user_id
    account_id = transaction_create.account_id
    amount = transaction_create.amount

    user = await user_db.get_user(user_id)
    if not user:
        raise UserNotFoundError()

    account = await account_db.get_account(account_id)
    if not account:
        raise AccountNotFoundError()

    if account.user_id != user_id:
        raise AccountNotFoundError()

    await transaction_db.create_transaction(transaction_id, user_id, account_id, amount)
