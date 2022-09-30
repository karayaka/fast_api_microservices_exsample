import imp
from unicodedata import name
from fastapi import FastAPI,Depends
from schema import TokenData,Comment,CommentCreate, serializeList,CommentCountMessage as ccm
from aut2Hadler import get_current_user
from database import comments
from message_broker_handler import comment_count_message


app=FastAPI()

@app.get('/comments')
def index():
    return serializeList(comments.find())

@app.get('/comments/{id}')
def get_omments(id,current_user:TokenData=Depends(get_current_user)):
    print(current_user)    
    return {"id":id}

@app.post('/comments')
async def create_comment(request:CommentCreate,current_user:TokenData=Depends(get_current_user)):
    comment=Comment(
        blog_id=request.blog_id,
        comment=request.comment,
        user_id=current_user.id,
        user_name=current_user.name,
        user_surname=current_user.surname
    )
    
    comments.insert_one(dict(comment))
    cmm_cn=serializeList(comments.find())
    message=ccm(commetn_count=len(cmm_cn))
    await comment_count_message(message=message)
    return cmm_cn