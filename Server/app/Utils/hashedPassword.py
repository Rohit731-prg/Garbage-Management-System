from passlib.hash import pbkdf2_sha256

def hash_Password(password: str) -> str:
    return pbkdf2_sha256.hash(password)

def compare_Password(password: str, hashPassword: str) -> bool:
    return pbkdf2_sha256.verify(password, hashPassword)