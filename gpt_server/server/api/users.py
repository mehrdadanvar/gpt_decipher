from datetime import datetime as dt
from fastapi import  APIRouter, HTTPException, status
from pydantic import BaseModel,Field,root_validator,validator
import hashlib
from db import usersdatabase
import pymongo
user_collection = usersdatabase["users"]
print(usersdatabase)

router = APIRouter()


def generate_date():
    now = dt.now()
    return now.strftime("%Y-%m-%d %H:%M")

def hash_password(password):
    h = hashlib.new("SHA256")
    h.update((password).encode())
    return h.hexdigest()





class NewUser(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str 
    speciality: str
    activated: bool = False
    created_at: str = Field(default_factory=generate_date)

    @classmethod
    @root_validator(pre=True)
    def set_created_at(cls, values):
        if "created_at" not in values:
            values["created_at"] = generate_date()
        return values
        

def check_existence(user: NewUser)-> bool:
    item = user_collection.find_one({"email":user.email})
    return True if item else  False 
    

class LoginUser(BaseModel):
    email: str
    password: str


class LoggedUser(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    speciality: str
    activated: bool
    created_at: str





@router.get("/users")
async def read_users():
    return {"code": "code"}


@router.post("/users/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: NewUser): 
    has_account = check_existence(user)
    if has_account:
        raise HTTPException(409,{"code":"409","error": "User already exists",
                                    "message": "The user with the specified credentials already exists in the system."})
    else:
        hashed_password = hash_password(user.password)
        user.password = hashed_password
        x = user_collection.insert_one(user.dict())
        print(x.inserted_id)
        return {"code": "201", "message":f"successfully created an account for {user.email} "}

    # return {"message":"user"}


@router.post("/users/login")
async def login(user: LoginUser):
    login_collection = usersdatabase["users"]
    retrieved = login_collection.find_one({"email": user.email})
    hashed_password = hash_password(user)
    gpt = LoggedUser(**retrieved)
    if hashed_password == retrieved["password"]:
        to_return = {
            "firstname": retrieved["firstname"],
            "lastname": retrieved["lastname"],
            "email": retrieved["email"],
            "speciality": retrieved["speciality"],
            "activated": retrieved["activated"],
        }
        print("hoooray")
        return {"user_object": to_return}
    else:
        print("faild")
        return {"message": "success"}
