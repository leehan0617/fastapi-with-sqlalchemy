from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from dependencies.get_db import get_db
from model.login_user_model import LoginUser
from schema.login_user_schema import LoginUserCreate, LoginUserRequest
from component.login_manager import encrypt_password, decrypt_password
from component.token_manager import create_jwt

router = APIRouter()


@router.post('/login-user')
def create_login_user(user: LoginUserCreate, db: Session = Depends(get_db)):
    print(user)
    encoded_password = encrypt_password(user.password)
    login_user = LoginUser(
        id=user.id, password=encoded_password, description=user.description)
    db.add(login_user)
    db.commit()
    # db.refresh(login_user)
    return login_user


@router.post('/login')
def login(response: Response, user: LoginUserRequest, db: Session = Depends(get_db)):
    db_user = db.query(LoginUser).filter_by(id=user.id).first()
    if (db_user is not None and decrypt_password(user.password, db_user.password)):
        token = create_jwt(db_user.id)
        response.set_cookie(key='auth_token', value=token)
        db.commit()
        return db_user
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'message': 'invalid login'}
