from fastapi import FastAPI, APIRouter, Response
from db import questionsdatabase
from pydantic import BaseModel
import pprint

collection = questionsdatabase["sevemteenhubdred"]
router = APIRouter()

# class Question(BaseModel):
#     id:int
#     title:str
#     options:list[str]
#     correct: list[str]



@router.get("/collections")
async def do_wantyouwant():
    documents =  collection.find().limit(10)
    questions = []
    for document in documents:
        print(document["id"])
        inter = {"id":document["id"],"title":document["title"],"options":document["options"],"correct":document["correct"]}
        questions.append(inter)
    return {"documents":questions}



