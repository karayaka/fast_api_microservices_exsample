from pyexpat import model
from turtle import title
from typing import List
from unicodedata import category
from fastapi import FastAPI,Depends,Response
import uvicorn
from schema import Blog,Category,BlogModel,User
import models
from database import engine,SesionLocal
from sqlalchemy.orm import Session
from aut2Hadler import get_current_user
import asyncio
from message_broker_handler import commet_count_consume


models.Base.metadata.create_all(engine)

app =FastAPI()

asyncio.create_task(commet_count_consume())


def get_db():
    db=SesionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/blogs',response_model=List[BlogModel])
def index(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blogs/{id}')
def get_blog(id,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    print(current_user)
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    return blog


@app.post('/blog')
def create_blog(blog:Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=blog.title,body=blog.body,category_id=blog.category_id)#DAHA KISA BİR YOLU VARMI!
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.post('/category')
def create_category(category:Category,db:Session=Depends(get_db)):
    new_category=models.Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return category

@app.get('/category')
def get_all_categorys(db:Session=Depends(get_db)):
    categorys=db.query(models.Category).all()
    return categorys


