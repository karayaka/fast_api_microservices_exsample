from code import interact
from email.policy import default
from turtle import back
from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True)
    title=Column(String)
    body=Column(String)
    comment_count=Column(Integer,default=0)
    category_id=Column(Integer,ForeignKey("categorys.id"))
    category=relationship("Category",back_populates="blogs")


class Category(Base):
    __tablename__='categorys'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    blogs=relationship("Blog",back_populates="category")
    