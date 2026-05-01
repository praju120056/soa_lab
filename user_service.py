# user_service.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory DB
users = []

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}

@app.get("/users")
def get_users():
    return users