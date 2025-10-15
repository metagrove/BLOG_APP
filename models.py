from sqlalchemy import Column, Integer, String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    body  = Column(String)
    user_id = Column(Integer,ForeignKey('userinfotable.id'))
    creator = relationship("usertable",back_populates="blog")


class usertable(Base):
    __tablename__ = "userinfotable"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blog = relationship("Blog",back_populates="creator")
