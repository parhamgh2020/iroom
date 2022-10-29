from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
  username: str
  email: str
  password: str
  national_code: int
  phone: str

class User(BaseModel):
  id: int
  username: str
  class Config():
    orm_mode = True


class UserDisplay(BaseModel):
    username: str
    email: str
    password: str
    national_code: int
    phone: str