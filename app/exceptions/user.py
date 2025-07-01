class AuthenticationError(Exception):
    def __str__(self):
        return "Ошибка аутентификации: проверьте содержимое HTTP заголовков email и password"


class PermissionDenied(Exception):
    def __str__(self):
        return "Нет прав для доступа к этому ресурсу"


class EmailAlreadyExistsError(Exception):
    def __init__(self, email: str):
        self.email = email

    def __str__(self):
        return f"Email {self.email} уже используется."