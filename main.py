from fastapi import FastAPI, BackgroundTasks
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from routes.route import router
import os



app = FastAPI()
app.include_router(router)

# Load environment variables
load_dotenv()

# Port
port = int(os.getenv("PORT"))

# uvicorn main:app --reload