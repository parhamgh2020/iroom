from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        firstname=request.firstname,
        lastname=request.lastname,
        email=request.email,
        phone_number=request.phone_number,
        national_code=request.national_code,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(status_code=201, content=jsonable_encoder(new_user))


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, _id: int):
    user = db.query(DbUser).filter(DbUser.id == _id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {_id} not found')
    return user


def get_user_by_firstname(db: Session, firstname: str):
    user = db.query(DbUser).filter(DbUser.firstname == firstname).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with firstname {firstname} not found')
    return user


def update_user(db: Session, _id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == _id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {_id} not found')
    user.update({
        DbUser.firstname: request.firstname,
        DbUser.lastname: request.lastname,
        DbUser.national_code: request.national_code,
        DbUser.phone_number: request.phone_number,
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, _id: int):
    user = db.query(DbUser).filter(DbUser.id == _id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {_id} not found')
    db.delete(user)
    db.commit()
    return 'ok'



