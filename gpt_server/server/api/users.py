from datetime import datetime as dt
from fastapi import FastAPI, APIRouter, Response
from pydantic import BaseModel,Field
from bson import ObjectId
import hashlib
from db import usersdatabase

print(usersdatabase)

router = APIRouter()


def generate_date():
    now = dt.now()
    return now.strftime("%Y-%m-%d %H:%M")

class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    speciality: str

class LoginUser(BaseModel):
    email: str
    password: str

class LoggedUser(BaseModel):
    id: ObjectId
    firstname: str
    lastname: str
    email: str
    password: str
    speciality: str
    activated: bool
    created_at : str


@router.get("/users")
async def read_users():
    return {"message":"All users"}

@router.post("/users")
async def create_user(user:User):
    print(user)
    user_collection = usersdatabase["users"]
    h = hashlib.new("SHA256")
    h.update((user.password).encode())
    hashed_pass = h.hexdigest()
    print(hashed_pass)
    to_be_inserted = {"firstname":user.firstname,
        "lastname":user.lastname,
        "email":user.email,
        "password":hashed_pass,
        "speciality":user.speciality,
        "activated": False,
        "created_at":generate_date()}
    print(to_be_inserted)
    x = user_collection.insert_one(to_be_inserted)
    print(x.inserted_id)
    return {"user":"test"}
    
    # return {"message":"user"}
@router.post("/users/login")
async def login(user:LoginUser):
    print("successfully hit the rout")
    print(user)
    login_collection = usersdatabase["users"]
    retrieved = login_collection.find_one({"email":user.email})
    print(retrieved)
    print(type(retrieved))
    h = hashlib.new("SHA256")
    h.update((user.password).encode())
    print(h)
    hashed_pass = h.hexdigest()
    print(hashed_pass)
    print(retrieved["lastname"])
    gpt = LoggedUser(**retrieved)
    if hashed_pass == retrieved["password"]:
        to_return = {
            "firstname":retrieved["firstname"],
        "lastname":retrieved["lastname"],
        "email":retrieved["email"],
        "speciality":retrieved["speciality"],
        "activated": retrieved["activated"],
        }
        print("hoooray")
        return {"user_object":to_return}
    else:
        print("faild")
        return {"message":"success"}
