from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def index():
  return {"message" : "Hello World"}

@app.get("/countries/japan")
async def country():
  return {"message": "this is japan!"}

@app.get("/countries/{country_name}")
async def country(country_name: str = "japan", city_name: str = "tokyo"):
  return {"country_name": country_name, "city_name": city_name}

@app.get("/countries")
async def country(country_name: str = "japan", country_no: Optional[int] = None):
  return {
    "country_name": country_name,
    "country_no": country_no
  }

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: int
  tax: Optional[float] = None

"""
sample item
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
"""

@app.post("/item")
async def create_item(item: Item):
  return {"message": f"{item.name}は、税込価格{int(item.price*(1 + item.tax))}円です。"}
