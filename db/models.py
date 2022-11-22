from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, Float

from db.database import Base, engine


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    national_code = Column(String, unique=True)
    phone_number = Column(String, unique=True)


class DbReception(Base):
    __tablename__ = 'reception'
    id = Column(Integer, primary_key=True, index=True)
    room = Column(Integer, ForeignKey("user.id"))
    start_inhabiting = Column(Date)
    end_inhabiting = Column(Date)
    status = Column(String)
    price = Column(Float)
    off = Column(Float)


class DbRoom(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    capacity = Column(Integer)
    floor = Column(Integer)
    room_number = Column(Integer)


DbUser.metadata.create_all(bind=engine)
