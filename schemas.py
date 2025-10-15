from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title:str
    body :str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name : str
    email : str
    password : str 

class Showonlyuser(BaseModel):
    name : str
    email: str
    blog : List[Blog] =[]
    class Config():
        orm_mode = True

class show_fields(BaseModel):
    title: str
    body : str 
    creator : Showonlyuser
    class Config():
        orm_mode = True


class Login(BaseModel):
    username :str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None