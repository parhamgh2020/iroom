from typing import List, Union
from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from auth.oauth2 import get_athenticated_user

router = APIRouter(
    prefix='/room',
    tags=['room']
)


@router.get('/')
def get_all_users(token: Union[str, None] = Header(default=None), db: Session = Depends(get_db)):
    user = get_athenticated_user(token, db)
    return {
        'room': 101,
        'vip': True,
        'user': user
    }
