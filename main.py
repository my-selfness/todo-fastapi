from fastapi import FastAPI
from routes import todo_route,auth_route

app = FastAPI()
app.include_router(todo_route.router)
app.include_router(auth_route.authrouter)




# uvicorn main:app --reload