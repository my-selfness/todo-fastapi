from pydantic import BaseModel,Field
from datetime import datetime




class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    name: str
    email: str
    password:str
    created_at: datetime = Field(default_factory=datetime.now)

class Todo(BaseModel):
    user= str
    title: str
    description: str
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
