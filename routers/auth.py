
from fastapi import APIRouter,Response,  status, HTTPException, Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from fastApi import schemas
from fastApi.oauth2 import ACCESS_TOKEN_EXPIRE_MINUTES

from ..database import  get_db
from .. import models, utils, oauth2


router = APIRouter()

@router.post("/login", tags=['auth'])
def login(user_credentials : schemas.CreateUser, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="user not found")
    
    if utils.encript(user_credentials.password) != user.password:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="user not found")

    ACCESS_TOKEN = oauth2.create_access_token(data = {"user_id":user.id})
    return {"token" : ACCESS_TOKEN}
    