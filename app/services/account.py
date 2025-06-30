from app.database import account
from app.schemas.account import AccountWithBalance


async def get_accounts_with_balance(user_id: int) -> list[AccountWithBalance]:
    """Возвращает список моделей AccountWithBalance"""
    rows = await account.get_accounts_with_balance(user_id)
    return [AccountWithBalance(**row._mapping) for row in rows]
