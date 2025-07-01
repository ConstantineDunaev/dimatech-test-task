from hashlib import sha256


def get_hash(text: str) -> str:
    """Возвращает хэш строки"""
    return sha256(text.encode('utf-8')).hexdigest()


def verify_password(password: str, hast_password: str) -> bool:
    """Сверяет хэши паролей"""
    new_hash_password = get_hash(password)
    return hast_password == new_hash_password
