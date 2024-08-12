from fastapi import APIRouter,Depends
from typing import Annotated
from models.todo import Todo
from db.db import collection_name
from schema.schema import list_serial
from bson import ObjectId
from controller.todo import get_user_id


router = APIRouter(prefix="/api")

# Get Request Methdos
@router.get("/todo/",tags=["Todo"])
async def get_todos(user_id:Annotated[ str , Depends(get_user_id)]):
    todos=list_serial(collection_name.find({"user_id":user_id}))
    return todos

# post request method
@router.post("/todo/",tags=["Todo"])
async def post_todo(user_id:Annotated[ str , Depends(get_user_id)] , todo: Todo):
    mytodo={
        "user_id":user_id,
        "title":todo.title,
        "description":todo.description,
        "completed":todo.completed,
        "created_at":todo.created_at
    }
    collection_name.insert_one(mytodo)
    return{"message":"Todo Added Successfully"}

# put request method for update
@router.put("/todo/{id}",tags=["Todo"])
async def put_todo(id:str,todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    return{"message":"Todo Updated Successfully"}

# delete request method
@router.delete("/todo/{id}",tags=["Todo"])
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return{"message":"Todo Deleted Successfully"}


# TODO: get only the logged in user todo