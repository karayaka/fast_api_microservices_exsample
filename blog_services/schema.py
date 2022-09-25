from typing import Optional,Union
from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
    category_id:int

class Category(BaseModel):
    name:str
    class Config():
        orm_mode=True

class BlogModel(BaseModel):
    title:str
    body:str
    category:Category    
    class Config():
        orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None

class User(BaseModel):
    name:str
    surname:str
    email:str
    password:str