
from datetime import datetime, timedelta
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .config import SettingsConfig


settings = SettingsConfig()

print(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
print(settings.SECRET_KEY)
print(settings.ALGORITHM)

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2pwdbarear = OAuth2PasswordBearer(tokenUrl= 'login')

def create_access_token(data: dict, ) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow()+ timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp'] = expire
    return jwt.encode(claims =to_encode, algorithm=ALGORITHM, key= SECRET_KEY,)

def verify_access_token(token : str, credentials_exception):
    pass    

def create_user(token = Depends(oauth2pwdbarear)):
    print("from create user")
    credentials_exception = HTTPException(
        status_code= 401,
        detail='Unauthorized action',
        headers= {"WWW-authenticate" : "Bearer"})
    try:
        data = jwt.decode(token = token,key= SECRET_KEY, algorithms= ALGORITHM)
        print(data)
        id = data['user_id']
        if not id:
            print("wrong id ")
            raise credentials_exception
        return id
    except JWTError as e:
        print("from try except ")
        print(e)
        raise credentials_exception