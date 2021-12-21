
from typing import List
from fastapi import APIRouter,Response,  status, HTTPException, Depends
from sqlalchemy.orm import Session
# from sqlalchemy.sql.functions import user
import app.schemas as schemas, app.oauth2 as oauth2

from app.schemas import Post, Post_response
from app.database import  get_db
import app.models as models

router = APIRouter()

@router.get("/posts",  response_model= List[Post_response],tags= ['posts'])
async def get_posts(db: Session = Depends(get_db)):
    return  db.query(models.Post).all()

@router.get('/posts/{id}',response_model= Post_response, tags= ['posts'])
async def get_post(id : int, db: Session = Depends(get_db)):
    return  db.query(models.Post).filter(models.Post.id == id).first()
    

@router.post("/create", status_code= status.HTTP_201_CREATED,  response_model= Post_response,tags= ['posts'])
async def add_post(post: schemas.Post, db: Session = Depends(get_db),user_id = Depends(oauth2.create_user)):
    print(user_id)
    # post = post.dict()
    # print("====================================")
    db_post = models.Post(**post.dict())
    db_post.ownerId = user_id
    print(db_post.content, db_post.id, db_post.ownerId, db_post.published)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return  db_post

@router.delete( "/delete/{id}",status_code = status.HTTP_204_NO_CONTENT,tags= ['posts'])
async def delete(id : int, db:Session = Depends(get_db),user_id = Depends(oauth2.create_user)):
    print(user_id)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if post:
        if  post.ownerId == user_id:
            post.delete(synchronize_session= False)
            db.commit()
            return Response(status_code = status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail= 'cant delete other s posts')

    else :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'post not found')

@router.put("/posts/{id}", response_model= schemas.Post, tags= ['posts'])
async def update_post(id: int, new_post: Post, db :Session = Depends(get_db), user_id : int = Depends(oauth2.create_user)):
    # print(user_id)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    mpost = post_query.first()
    
    if mpost:
        if mpost.ownerId == user_id :
            post_query.update(new_post.dict(), synchronize_session= False )
            db.commit()
            return  new_post
        else :
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail= 'can t modify other s posts')

    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'post not found')
