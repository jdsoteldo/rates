import requests
import json

url = 'https://api.yadio.io/rate/usd'

response = requests.get(url)
format = response.json()["rate"]
print(format)
