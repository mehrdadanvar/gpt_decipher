import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
secret = os.getenv("MONGO_URI")
print(secret)
client = MongoClient(secret)
print("client connected")
questionsdatabase = client["questions"]
names = questionsdatabase.list_collection_names()
for item in names:
    print("heyyyyyyyyyyyyyyyyyyyyyy",item)
usersdatabase = client["users"]
newnames = usersdatabase.list_collection_names()
for i in newnames:
    print(i,"usssssssssssser database")