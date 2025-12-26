from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name:str
    price:float
    tax:Optional[float] = None
    
app = FastAPI()

@app.get("/message/{username}")

def welcome(username:str):
    return {"msg":f"Welcome {username}"}

@app.get("/item-details/{item}")

def item_details(item:str,company:str|None = None):
    return{"Item-Name":item,"Company":company}


@app.get("/items")

async def get_items(skip:int=0,limit:int=10):
    dummy_data = [
        {"name":"Lappy 1","price":100},
        {"name":"Lappy 2","price":200},
        {"name":"Lappy 3","price":300,"tax":"10%"},
        {"name":"Lappy 4","price":400},
        {"name":"Lappy 5","price":500},
    ]
    
    return dummy_data[skip:skip+limit]
