class InvalidSingnatureError(Exception):
    def __str__(self):
        return "Неверная подпись запроса"
