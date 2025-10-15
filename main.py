from fastapi import FastAPI, Depends,status,Response,HTTPException
from . import schemas,models
from . import hashing
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from .routers import blogs,users,auth

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(auth.router)
app.include_router(blogs.router)
app.include_router(users.router)



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post("/blog",tags=["Blogs"])
# def create(request : schemas.Blog,db :Session = Depends(get_db),tags=["Blogs"]):
#     new_blog=models.Blog(title=request.tile,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get("/blog_get",response_model =List[schemas.show_fields],tags=["Blogs"])
# def all_blog(db :Session = Depends(get_db)):
#     blogs = db.execute(text("SELECT * FROM Blogs"))
#     db_blog = [dict(x) for x in blogs.mappings().all()]
#     return db_blog

# @app.get("/blog_get")
# def all_blogs(db :Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get("/blogs/{id}",status_code=200,tags=["Blogs"])
# def search_blog(id, response:Response, db :Session = Depends(get_db)):

#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"deatils" : "not founded"}
#         raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,details="Not found")
    
#     return blogs



# @app.delete("/blog_post_delete/{delete_id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
# def delete_blog(delete_id, db :Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id ==delete_id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry {delete_id} is not found!")
#     blog.delete(synchronize_session =False)
#     db.commit()
#     return {"message":"Successfully deleted"}
    
    
# @app.put("/blog_update/{id_update}",status_code =status.HTTP_202_ACCEPTED,tags=["Blogs"])
# def update_blog(id_update, request:schemas.Blog, db :Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id ==id_update)
#     blog_f = blog.first()
#     if not blog_f:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry {id_update} is not found!")
    
#     blog.update(request.model_dump())
#     db.commit()
    
#     return "Update was manifested"


# @app.post('/user',response_model=schemas.Showonlyuser,tags=["User"])
# def create_new_user(request :schemas.User,db :Session = Depends(get_db)):
#     new_user = models.usertable(name = request.name,
#                            email = request.email,
#                            password =hashing.HASH.Bcypt(request.password) )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{user_id}',response_model=schemas.Showonlyuser,tags=["User"])
# def get_user(user_id:int,db :Session = Depends(get_db)):
#     user = db.query(models.usertable).filter(models.usertable.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry {user_id} is not found!")
    
#     db.commit()
#     return user