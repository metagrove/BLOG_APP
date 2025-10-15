from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from .. import models

def get_all(db:Session):
    #blogs = db.execute(text("SELECT * FROM Blogs"))
    # db_blog = [dict(x) for x in blogs.mappings().all()]
    db_blog = db.query(models.Blog).all()
    return db_blog