from controller.auth import verify_token
from fastapi import Depends
from models.todo import UserOut




async def get_user_id(user: dict = Depends(verify_token)):
    return user["_id"]