class AuthenticationError(Exception):
    def __str__(self):
        return "Ошибка аутентификации: проверьте содержимое HTTP заголовков email и password"
