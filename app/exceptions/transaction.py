class TransactionIDAlreadyExistsError(Exception):
    def __init__(self, transaction_id: str):
        self.transaction_id = transaction_id

    def __str__(self):
        return f"Транзакция ID {self.transaction_id} уже существует."
