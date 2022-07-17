from email import message
import re
import string
from fastapi import FastAPI

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
async def country(country_name: str = "japan", country_no: int = 1):
  return {
    "country_name": country_name,
    "country_no": country_no
  }
