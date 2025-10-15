from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import text
from .. import schemas,models,hashing
from ..repository import user


router = APIRouter(
    prefix= "/user",
    tags = ["User"]  
)

get_db=database.get_db

@router.post('/',response_model=schemas.Showonlyuser)
def create_new_user(request :schemas.User,db :Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/user/{user_id}',response_model=schemas.Showonlyuser)
def get_user(user_id:int,db :Session = Depends(get_db)):
    user = db.query(models.usertable).filter(models.usertable.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry {user_id} is not found!")
    
    db.commit()
    return user