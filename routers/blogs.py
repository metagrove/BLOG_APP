from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,models
from sqlalchemy import text
from ..repository import blog
from blog import oauth2
router = APIRouter()
get_db=database.get_db

@router.post("/blog",tags=["Blogs"])
def create(request : schemas.Blog,db :Session = Depends(get_db),tags=["Blogs"]):
    new_blog=models.Blog(title=request.title,body=request.body,user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog_get",response_model =List[schemas.show_fields],tags=["Blogs"])
def all_blog(db :Session = Depends(database.get_db),get_current_user :schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get("/blogs/{id}",status_code=200,tags=["Blogs"])
def search_blog(id, response:Response, db :Session = Depends(get_db)):

    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"deatils" : "not founded"}
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,details="Not found")
    return blogs


@router.delete("/blog_post_delete/{delete_id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def delete_blog(delete_id, db :Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==delete_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry {delete_id} is not found!")
    blog.delete(synchronize_session =False)
    db.commit()
    return {"message":"Successfully deleted"}
    
@router.put("/blog_update/{id_update}",status_code =status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update_blog(id_update, request:schemas.Blog, db :Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id_update)
    blog_f = blog.first()
    if not blog_f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry {id_update} is not found!")
    
    blog.update(request.model_dump())
    db.commit()
    
    return "Update was manifested"
