import requests
import json

url = 'https://s3.amazonaws.com/dolartoday/data.json'

response = requests.get(url)
format = response.json()["USD"]["transferencia"]
print(format)