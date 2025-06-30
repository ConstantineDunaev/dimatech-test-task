from hashlib import sha256


def verify_password(password: str, hast_password: str) -> bool:
    """Сверяет хэши паролей"""
    new_hash_password = sha256(password.encode()).hexdigest()
    return hast_password == new_hash_password
