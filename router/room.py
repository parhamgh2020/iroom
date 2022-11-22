import traceback
from typing import List, Union
from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_room
from auth.oauth2 import get_authenticated_user
from schemas import RoomBase

router = APIRouter(
    prefix='/room',
    tags=['room']
)


@router.get('/test_auth')
def get_all_rooms(token: Union[str, None] = Header(default=None), db: Session = Depends(get_db)):
    user = get_authenticated_user(token, db)
    return {
        'room': 101,
        'vip': True,
        'user': user
    }


@router.post('/')
def create_room(request: RoomBase, db: Session = Depends(get_db)):
    try:
        output = db_room.create_room(db, request)
        return output
    except Exception as exp:
        return JSONResponse(
            status_code=500,
            content=traceback.format_exc()
        )


# Read all users


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return db_room.get_all_rooms(db)


# Read one user


@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return db_room.get_room(db, id)


# Update user


@router.put('/{id}/update')
def update_room(id: int, request: RoomBase, db: Session = Depends(get_db)):
    return db_room.update_room(db, id, request)


# Delete user


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_room.delete_room(db, id)
