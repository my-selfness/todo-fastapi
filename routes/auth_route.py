from db.db import user_collection
from models.todo import User,Token
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
import os
from auth_logic.auth import authenticate_user,create_access_token,hash_password
from datetime import  timedelta



authrouter = APIRouter(prefix="/api/auth")


# load dotenv
load_dotenv()




# user register
@authrouter.post("/register")
async def register_user(user_data: User):
    if user_collection.find_one({"email":user_data.email}):
        return {"message": "User already exists"}
    hashed_password = hash_password(user_data.password)
    # Save user data
    user_doc = {
        "name": user_data.name,
        "email": user_data.email,
        "password": hashed_password,
        "created_at": user_data.created_at
    }
    user_collection.insert_one(user_doc)
    return {"message": "User registered successfully"}




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # user login
@authrouter.post("/token") 
async def login_for_access_token(
    form_data: Annotated[str, Depends(oauth2_scheme)],
) -> Token:
    user = authenticate_user(user_collection, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES")))
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")