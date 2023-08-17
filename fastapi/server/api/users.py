from datetime import datetime as dt
from fastapi import  APIRouter, HTTPException, status , Response
from pydantic import BaseModel,Field,root_validator,validator
import hashlib
from db import usersdatabase
from auth import generate_token
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
    specialty: str
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
    return True if item else False 
    

class LoginUser(BaseModel):
    email: str
    password: str


class LoggedUser(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    specialty: str
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
        return {"code": 201, "message":f"successfully created an account for {user.email} "}



@router.post("/users/login", status_code=status.HTTP_200_OK)
async def login(user: LoginUser,response:Response):
    match(user.email,user.password):
        case("",""):
            raise HTTPException(400,{"code":400,"error":"Bad Request","message":"Please provide both email and password for login."})
    retrieved = user_collection.find_one({"email":user.email})
    claiming_hash = hash_password(user.password)
    match (retrieved):
        case (None):
            raise HTTPException(404,detail={"code":404, "error":"Unauthorized","message":f"Log in failed because there was no account associated with {user.email}"})
    match(retrieved["email"]==user.email,claiming_hash ==retrieved["password"]):
        case(True,False):
            raise HTTPException(401,{"code":401,"error":"Unauthorized","message":"Incorrect password. Please try again."})
        case (True,True):
            response.set_cookie(key="jwt", value = generate_token(user),httponly=True)
            return {"code":200,"message":"Successful Login"}



    
