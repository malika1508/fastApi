from pydantic import BaseModel, EmailStr


#hello this is a modification
class Post(BaseModel):
    title : str
    content : str
    published : bool
    class Config:
        orm_mode = True

class Post_response(BaseModel):
    id: int
    title : str
    content : str
    published : bool
    ownerId : int
    class Config:
        orm_mode = True

class User(BaseModel):
    id : int
    email: EmailStr
    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    email:str
    password: str

class Token(BaseModel):
    access_token: str
    token_type : str
    class Config:
        orm_mode = True