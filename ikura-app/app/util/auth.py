"""module auth
"""
import bcrypt


def get_hash(str: str) -> bool:
    """Generates a hashed password"""
    return bcrypt.hashpw(str.encode(), bcrypt.gensalt())


def validate(pw: str, hash: str) -> bool:
    """check if pw matches the hashed str"""
    return bcrypt.checkpw(pw.encode(), hash.encode())
