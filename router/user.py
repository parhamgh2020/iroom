from typing import List
from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create user


# @router.post('/', response_model=UserDisplay)
@router.post('/')
def create_user(request: UserBase, db: Session = Depends(get_db)):
    try:
        output = db_user.create_user(db, request)
        return output
    except Exception as exp:
        return JSONResponse(
            status_code=500,
            content=str(exp)
        )
# Read all users


@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), auth: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)

# Read one user


@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# Update user


@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete user


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
