from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hi i  am a FastAapi server"}

@app.get("/hello/{name}")
def hello_name(name:str ):
    return {"message": f"Hi, {name}"}

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"received": item, "message": "Add"}
