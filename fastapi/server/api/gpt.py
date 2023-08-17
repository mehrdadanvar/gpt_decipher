import os
import openai
import requests as r
from fastapi import  APIRouter, HTTPException, status , Response
from pydantic import BaseModel
from time import sleep
router = APIRouter()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization =os.getenv("ORGANIZATION")

def request_gpt(question:str):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": question}])
    chat_response = completion.choices[0].message
    return chat_response




class GPTQuery(BaseModel):
    query : str

@router.post("/gpt/index")
async def call_gpt(query:GPTQuery):
    print(query)
    normal_text = query.dict()
    print(normal_text)
    print(normal_text["query"])
    res = request_gpt(normal_text["query"])
    print(type(res),res)
    try:
        return {"message": res["content"]}
    except:
        print("some error")
    return {"message": "hi"}