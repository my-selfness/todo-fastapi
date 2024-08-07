from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load env
load_dotenv()

# # Replace the placeholder with your Atlas connection string
uri = os.getenv("MONGODB_URI")


client=MongoClient(uri)

db=client.todo_db
user_db=client.todo_users

collection_name=db["todo_collection"]
user_collection=user_db["todo_user"]