from email import message
import re
import string
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
  return {"message" : "Hello World"}

@app.get("/countries/{country_name}")
async def country(country_name: str):
  return {"country_name": country_name}
