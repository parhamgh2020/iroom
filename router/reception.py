import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db import db_reception
from db.database import get_db
from schemas import ReceptionBase

router = APIRouter(
    prefix='/reception',
    tags=['reception']
)


@router.post('/')
def create_reception(request: ReceptionBase, db: Session = Depends(get_db)):
    try:
        output = db_reception.create_reception(db, request)
        return output
    except Exception as exp:
        return JSONResponse(
            status_code=500,
            content=traceback.format_exc()
        )


# Read all users


@router.get('/')
def get_all_reception(db: Session = Depends(get_db)):
    return db_reception.get_all_receptions(db)


# Read one user


@router.get('/{_id}')
def get_reception(_id: int, db: Session = Depends(get_db)):
    return db_reception.get_reception(db, _id)


# Update user


@router.put('/{_id}/update')
def update_reception(_id: int, request: ReceptionBase, db: Session = Depends(get_db)):
    return db_reception.update_reception(db, _id, request)


# Delete user


@router.delete('/delete/{_id}')
def delete_reception(_id: int, db: Session = Depends(get_db)):
    return db_reception.delete_reception(db, _id)


@router.get('/get_by_user/{_id}')
def get_reception_by_user_id(_id: int, db: Session = Depends(get_db)):
    return db_reception.get_reception_by_user_id(db, _id)
