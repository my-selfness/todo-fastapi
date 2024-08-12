from pydantic import BaseModel,Field,EmailStr
from datetime import datetime




class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    name: str
    email: EmailStr
    password:str
    created_at: datetime = Field(default_factory=datetime.now)
class UserOut(BaseModel):
    _id=str
    name: str
    email: EmailStr
    password:str
    created_at: datetime = Field(default_factory=datetime.now)

class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

class TodoFront(BaseModel):
    user_token:str
    title: str
    description: str
    completed: bool = False
