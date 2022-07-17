import requests
import json

def main():
  url = 'http://127.0.0.1:8000/item'
  body = {
    "name": "Tshirts",
    "description": "Teppei KikuchiのTshirtsです。",
    "price": 45.2,
    "tax": 3.5
  }
  res = requests.post(url, json.dumps(body))
  print(res.json())

if __name__ == "__main__":
  main()