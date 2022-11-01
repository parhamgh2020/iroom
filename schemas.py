from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    national_code: str
    phone_number: str


class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class UserDisplay(BaseModel):
    firstname: str
    lastname: str
    email: str
    national_code: str
    phone_number: str
