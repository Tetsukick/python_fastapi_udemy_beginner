from email import message
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
  return {"message" : "Hello World"}