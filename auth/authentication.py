from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from db.hash import Hash
from auth import oauth2
from schemas import Auth

router = APIRouter(
  tags=['authentication']
)

@router.post('/token')
def get_token(request: Auth, db: Session = Depends(get_db)):
  user = db.query(models.DbUser).filter(models.DbUser.phone_number == request.phone_number).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  if not 1111 == request.sms_code:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
  
  access_token = oauth2.create_access_token(data={'sub': user.firstname})

  return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user_id': user.id,
    'firstname': user.firstname
  }
