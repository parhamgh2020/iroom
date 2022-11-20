from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base, engine
from sqlalchemy import Column


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    national_code = Column(String, unique=True)
    phone_number = Column(String , unique=True)


DbUser.metadata.create_all(bind=engine)