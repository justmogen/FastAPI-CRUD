from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal

# from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class CreatePost(PostBase):
    pass

class UserExit(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    

class PostRes(PostBase):
    id: int
    owner_id: int
    owner: UserExit
    
    class Config:
        from_attributes = True


class PostVote(BaseModel):
    Post: PostRes
    votes: int
    
    class Config:
        from_attributes = True
    
class CreateUser(BaseModel):
    email: EmailStr
    password: str
    
    
class LoginUser(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]