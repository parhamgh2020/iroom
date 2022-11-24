from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.models import DbReception, DbRoom, DbUser
from schemas import ReceptionBase


async def create_reception(db: Session, request: ReceptionBase):
    new_reception = DbReception(
        user_id=request.user_id,
        room_id=request.room_id,
        start_rent=request.start_rent,
        end_rent=request.end_rent,
        payment_status=request.payment_status,
        price=request.price,
        percentage_off=request.percentage_off,
        price_off=request.price_off,
    )
    db.add(new_reception)
    db.commit()
    db.refresh(new_reception)
    return JSONResponse(status_code=201, content=jsonable_encoder(new_reception))


async def get_all_receptions(db: Session):
    return db.query(DbReception).all()


async def get_reception(db: Session, _id: int):
    reception = db.query(DbReception).filter(DbReception.id == _id).first()
    if not reception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Reception with id {_id} not found')
    return reception


async def update_reception(db: Session, _id: int, request: ReceptionBase):
    reception = db.query(DbReception).filter(DbReception.id == _id)
    if not reception.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Reception with id {_id} not found')
    reception.update({
        "user_id": request.user_id,
        "room_id": request.room_id,
        "start_rent": request.start_rent,
        "end_rent": request.end_rent,
        "payment_status": request.payment_status,
        "price": request.price,
        "percentage_off": request.percentage_off,
        "price_off": request.price_off,
    })
    db.commit()
    return 'ok'


async def delete_reception(db: Session, _id: int):
    reception = db.query(DbReception).filter(DbReception.id == _id).first()
    if not reception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Reception with id {_id} not found')
    db.delete(reception)
    db.commit()
    return 'ok'


async def get_reception_by_user_id(db: Session, _id: int):
    reception = db.query(DbReception, DbUser, DbRoom).filter(DbReception.user_id == _id).all()
    if not reception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Reception with user id {_id} not found')
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(reception))
