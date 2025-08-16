from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, constr

app = FastAPI()

# Memory storage for registered users
users_db = []

class RegisterModel(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8)

@app.post("/register")
def register_user(user: RegisterModel):
    # Save user to in-memory list
    users_db.append(user.dict())
    return {"message": "User registered successfully", "user": user}

@app.get("/users")
def get_users():
    return {"registered_users": users_db}
