from datetime import datetime, date, timedelta
from typing import Literal

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


class Auth(BaseModel):
    phone_number: str
    national_code: str
    sms_code: int = 1111


class RoomBase(BaseModel):
    type: str
    capacity: int
    floor: float
    room_number: int


class ReceptionBase(BaseModel):
    user_id: int = 1
    room_id: int = 1
    start_rent: date = datetime.now().date()
    end_rent: date = (datetime.now() + timedelta(days=1)).date()
    payment_status: Literal['paid', 'not_paid']
    price: int = 1000
    percentage_off: float = 0
    price_off: float = 0
