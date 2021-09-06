from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    id: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    description: str

    class Config:
        orm_mode = True
