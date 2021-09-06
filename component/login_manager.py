import bcrypt


def encrypt_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def decrypt_password(input_password: str, origin_password: str):
    return bcrypt.checkpw(input_password.encode('utf-8'), origin_password.encode('utf-8'))
