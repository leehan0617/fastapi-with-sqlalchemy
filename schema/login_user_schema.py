from pydantic import BaseModel

class LoginUserBase(BaseModel):
    id: str

class LoginUserCreate(LoginUserBase):
    password: str
    type: str
    description: str

    class Config:
        orm_mode = True

class LoginUserRequest(LoginUserBase):
    password: str
    
    class Config:
        orm_mode = True
