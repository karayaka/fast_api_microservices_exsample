from pydantic import BaseModel
from typing import Union

'''
    Bütün Objeleri Serilaze etmek için yaızlan kod
'''
def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}
'''
    Bütün Obje Listelerini serlaze etmek için yazılan kod
'''
def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


class TokenData(BaseModel):
    email: Union[str, None] = None
    id: Union[str, None] = None
    name:Union[str, None] = None
    surname:Union[str, None] = None

class Comment(BaseModel):
    blog_id:int
    user_id:str
    user_name:str
    user_surname:str
    comment:str
class CommentCreate(BaseModel):
    blog_id:int
    comment:str

class CommentCountMessage(BaseModel):
    commetn_count:int
