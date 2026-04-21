from pydantic import BaseModel
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hi i am a FastApi server"}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hi, {name}"}

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"received": item, "message": "Add"}

@app.get("/items/", response_class=HTMLResponse)
async def show_item_form():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Добавить предмет</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            input { margin: 5px; padding: 8px; }
        </style>
    </head>
    <body>
        <h2>Добавить новый предмет (POST форма)</h2>
        <form action="/items/" method="post">
            <label>Название:</label><br>
            <input type="text" name="name" value="Кружка"><br>
            <label>Цена:</label><br>
            <input type="number" step="0.01" name="price" value="12.99"><br>
            <label>В наличии:</label>
            <input type="checkbox" name="in_stock" checked><br><br>
            <input type="submit" value="Отправить POST запрос">
        </form>
        <p><small>Если откроете просто в браузере - увидите эту форму.<br> 
        Чтобы увидеть JSON ответ, используйте /docs</small></p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
