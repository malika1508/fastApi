
from fastapi import FastAPI, Depends

from .database import engine, get_db
from routers import post, auth
import routers.user 
from fastapi.middleware.cors import CORSMiddleware
from .models import * 


# uvicorn app.main:app --reload



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)



@app.get("/")
async def root():
    return {"message": "Hello World"}



app.include_router(post .router)
app.include_router(routers.user.router)
app.include_router(auth.router)



# @app.get("/posts",  response_model= List[Post])
# async def get_posts(db: Session = Depends(get_db)):
#     # cur.execute(""" select * from post """)
#     # res = cur.fetchall()
#     # conn.commit()
#     return res

# @app.get('/posts/{id}', response_model= Post)
# async def get_post(id : int, db: Session = Depends(get_db)):
#     # cur.execute("select * from post where id = %s", (str(id),))
#     # res = cur.fetchone()
#     # conn.commit()
#     # if res:
#     #     return(res)
#     # raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "{status.HTTP_404_NOT_FOUND} id not found")
#     res = db.query(models.Post).filter(models.Post.id == id).first()
#     return res

# @app.post("/create", status_code= status.HTTP_201_CREATED,  response_model= Post)
# async def add_post(post: Post, db: Session = Depends(get_db)):
#     # try:
#     #     cur.execute("""INSERT INTO post (title, content,published)  VALUES (%s, %s, %s) Returning * """, 
#     #                     ( payload['title'], payload['content'], payload['published']))
#     #     res = cur.fetchone()
#     #     conn.commit()
#     #     return {"added" : res}
#     # except Exception as e:
#     #     raise e
#     # db_user = models.Post(title = post.title, content = post.content, published = post.published)
#     db_post = models.Post(**post.dict())
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return  db_post

# @app.delete("/delete/{id}",  status_code = status.HTTP_204_NO_CONTENT)
# async def delete(id : int, db:Session = Depends(get_db)):
#     #do something
#     # cur.execute(" DELETE FROM post where id = %s returning * ", (str(id),))
#     # posts = cur.fetchone()
#     post = db.query(models.Post).filter(models.Post.id == id)
    
#     if post.first():
#         post.delete(synchronize_session= False)
#         db.commit()
#         return Response(status_code = status.HTTP_204_NO_CONTENT)

#     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'id not found')

# @app.put("/posts/{id}", response_model= Post)
# async def update_post(id: int, new_post: Post, db = Depends(get_db)):
#     # cur.execute(" UPDATE post SET title = %s , content = %s , published = %s where id = %s returning *", 
#     # (payload['title'], payload['content'], payload['published'], str(id)))
#     # res = cur.fetchone()
#     # conn.commit()
#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     if post_query.first():
#         post_query.update(new_post.dict(), synchronize_session= False )
#         db.commit()
#         return  new_post
#     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'id not found')


# @app.put("/users", response_model= schemas.User)
# def add_user(payload : dict = Body(...), db : Session = Depends(get_db)):
#     user = models.User(email = payload['email'], password = payload['password'] )
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# @app.get('/user', response_model= schemas.User)
# def get_user(email: str, db : Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == email).first()
#     return user
