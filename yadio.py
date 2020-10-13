import requests
import json

# yadio

yadioUrl = 'https://api.yadio.io/rate/usd'

def yadio():
    response = requests.get(yadioUrl)
    format = response.json()["rate"]
    print("Yadio:", format)

yadio()
