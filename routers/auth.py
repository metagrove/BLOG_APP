from fastapi import APIRouter,Depends,status,HTTPException
from .. import  database,models,JWT_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..hashing import HASH

router = APIRouter(tags=["Authentication"])

get_db=database.get_db

@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):

    user = db.query(models.usertable).filter(models.usertable.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Sorry is not found!")
    if not HASH.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Incorrect chotu!")
     
    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWT_token.create_access_token(
        data={"sub": user.email},
    )
    return {"access_token":access_token, "token_type":"bearer"}