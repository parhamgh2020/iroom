from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from schemas import UserBase

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user


# @router.post('/', response_model=UserDisplay)
@router.post('/')
async def create_user(request: UserBase, db: Session = Depends(get_db)):
    try:
        output = db_user.create_user(db, request)
        return output
    except Exception as exp:
        return JSONResponse(
            status_code=500,
            content=str(exp)
        )


# Read all users


@router.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read one user


@router.get('/{_id}')
async def get_user(_id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, _id)


# Update user


@router.put('/{_id}/update')
async def update_user(_id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, _id, request)


# Delete user


@router.delete('/delete/{_id}')
async def delete(_id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, _id)
