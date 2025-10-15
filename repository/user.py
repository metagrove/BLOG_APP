from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from .. import models,schemas,hashing

def create_user(request:schemas.User,db:Session):
    new_user = models.usertable(name = request.name,
                           email = request.email,
                           password =hashing.HASH.Bcypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user