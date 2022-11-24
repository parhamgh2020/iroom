from typing import Union

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from router.reception import get_reception_by_user_id
from auth.oauth2 import get_authenticated_user
from db.database import get_db

router = APIRouter(
    prefix='/app',
    tags=['app']
)


@router.get('/login')
async def get_all_rooms(token: Union[str, None] = Header(default=None), db: Session = Depends(get_db)):
    user = get_authenticated_user(token, db)
    output = await get_reception_by_user_id(user.id, db)
    return output
