import logging
import jwt
import datetime


SECRET_KEY = 'ved_notiulos'


def create_jwt(id: str):
    return jwt.encode({
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60*12),
        'user_id': id
    }, SECRET_KEY, algorithm='HS256')


def validate_jwt(token: str):
    print('validate_jwt called')
    try:
        jwt.decode(token, SECRET_KEY, algorithms='HS256')
        return True
    except Exception as err:
        logging.error(err)
        return False
