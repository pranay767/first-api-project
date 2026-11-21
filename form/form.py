from pydantic import BaseModel

class UserBasePost(BaseModel):#input
    username:str

class UserBaseGet(BaseModel):#fetch from backend
    id: int
    username:str

class CommentBase(BaseModel):
    content:str
    user_id: int