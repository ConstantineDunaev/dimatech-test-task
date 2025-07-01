class AccountNotFoundError(Exception):
    def __init__(self, account_id: int):
        self.account_id = account_id

    def __str__(self):
        return f"Счет ID {self.account_id} не найден"
