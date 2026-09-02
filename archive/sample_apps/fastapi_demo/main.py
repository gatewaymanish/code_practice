from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    tax: float
    description: str


@app.get('/items')
async def home(item: Item):
    return item


