from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

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

class ShopInfo(BaseModel):
  name: str
  location: str


class Item(BaseModel):
  name: str = Field(min_length=4, max_length=12)
  description: Optional[str] = None
  price: int
  tax: Optional[float] = None

class Data(BaseModel):
  shop_info: Optional[ShopInfo]
  items: List[Item]

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

@app.post("/shop")
async def create_shop(data: Data):
  return {"data": data}
