from pydantic import BaseModel,Field
from datetime import datetime



class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    name: str
    email: str
    password:str
    todo: Todo | None = None
    refresh_token: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)

