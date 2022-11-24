import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db import db_room
from db.database import get_db
from schemas import RoomBase

router = APIRouter(
    prefix='/room',
    tags=['room']
)


@router.post('/')
async def create_room(request: RoomBase, db: Session = Depends(get_db)):
    try:
        output = db_room.create_room(db, request)
        return output
    except Exception as exp:
        print(traceback.format_exc())
        return JSONResponse(
            status_code=500,
            content=traceback.format_exc()
        )


# Read all users


@router.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    return db_room.get_all_rooms(db)


# Read one user


@router.get('/{_id}')
async def get_user(_id: int, db: Session = Depends(get_db)):
    return db_room.get_room(db, _id)


# Update user


@router.put('/{_id}/update')
async def update_room(_id: int, request: RoomBase, db: Session = Depends(get_db)):
    return db_room.update_room(db, _id, request)


# Delete user


@router.delete('/delete/{_id}')
async def delete(_id: int, db: Session = Depends(get_db)):
    return db_room.delete_room(db, _id)
