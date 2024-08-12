from passlib.context import CryptContext  
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends, HTTPException, status
from models.todo import UserOut
from db.db import user_collection

# load env
load_dotenv()
# password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt



def authenticate_user(user_collection, email: str, password: str):
    user = user_collection.find_one({"email": email})
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        user =user_collection.find_one({"email": decoded_token.get("sub")})
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return {
            "_id": user["_id"],
            "name": user["name"],
            "email": user["email"],
            "created_at": user["created_at"]
        }
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
