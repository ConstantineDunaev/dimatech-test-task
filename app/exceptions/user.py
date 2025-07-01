class AuthenticationError(Exception):
    def __str__(self):
        return "Ошибка аутентификации: проверьте содержимое HTTP заголовков email и password"


class PermissionDeniedError(Exception):
    def __str__(self):
        return "Нет прав для доступа к этому ресурсу"


class EmailAlreadyExistsError(Exception):
    def __init__(self, email: str):
        self.email = email

    def __str__(self):
        return f"Email {self.email} уже используется."


class UserNotFoundError(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

    def __str__(self):
        return f"Пользователь ID {self.user_id} не найден."


class UserHasAccountsError(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

    def __str__(self):
        return f"Пользователь ID {self.user_id} имеет активные счета."
