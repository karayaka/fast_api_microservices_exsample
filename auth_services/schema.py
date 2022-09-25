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

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None

class Login(BaseModel):
    email:str
    password:str