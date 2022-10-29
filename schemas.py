from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
  first_name: str
  last_name: str
  email: str
  national_code: int
  phone_number: str

class User(BaseModel):
  id: int
  username: str
  class Config():
    orm_mode = True


class UserDisplay(BaseModel):
  first_name: str
  last_name: str
  email: str
  national_code: int
  phone_number: str
