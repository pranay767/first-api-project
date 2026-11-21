from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated
from fastapi import Depends
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:314159@localhost:3306/blogapplication'

engine = create_engine(URL_DATABASE, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    with SessionLocal() as db:
        yield db

db_dependency = Annotated[Session,Depends(get_db)]

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))

def start_engine():
    Base.metadata.create_all(bind=engine)