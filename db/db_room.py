from sqlalchemy.orm.session import Session
from schemas import RoomBase
from db.models import DbRoom
from fastapi import HTTPException, status


def create_room(db: Session, request: RoomBase):
    new_room = DbRoom(
        type=request.type,
        capaciy=request.capaciy,
        floor=request.floor,
        room_number=request.room_number
    )
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room


def get_all_rooms(db: Session):
    return db.query(DbRoom).all()


def get_room(db: Session, id: int):
    room = db.query(DbRoom).filter(DbRoom.id == id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Room with id {id} not found')
    return room


def get_user_by_room_number(db: Session, room_number: int):
    room = db.query(DbRoom).filter(DbRoom.room_number == room_number).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Room with room_numberr {room_number} not found')
    return room


def update_room(db: Session, id: int, request: RoomBase):
    room = db.query(DbRoom).filter(DbRoom.id == id)
    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Room with id {id} not found')
    room.update({
        DbRoom.type: request.type,
        DbRoom.capaciy: request.capaciy,
        DbRoom.floor: request.floor,
        DbRoom.room_number: request.room_number
    })
    db.commit()
    return 'ok'


def delete_room(db: Session, id: int):
    room = db.query(DbRoom).filter(DbRoom.id == id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Room with id {id} not found')
    db.delete(room)
    db.commit()
    return 'ok'
