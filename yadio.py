import requests
import json

url = 'https://api.yadio.io/rate/usd'

def yadio():
    response = requests.get(url)
    format = response.json()["rate"]
    print(format)

yadio()
