

from fastapi import APIRouter, Depends
from fastapi.params import Body
from pydantic import utils
from sqlalchemy.orm import Session
from fastApi import schemas

from ..database import  get_db
from .. import models, utils

router = APIRouter()

@router.put("/users", response_model= schemas.User, tags= ['users'])
def add_user(payload : schemas.CreateUser, db : Session = Depends(get_db)):
    user = models.User(email = payload['email'], password = utils.encript(payload['password']) )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/users', response_model= schemas.User, tags= ['users'])
def get_user(email: str, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user
