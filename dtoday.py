import requests
import json

# Dolar today

dtUrl = 'https://s3.amazonaws.com/dolartoday/data.json'

def dolartoday():
    response = requests.get(dtUrl)
    format = response.json()["USD"]["transferencia"]
    print("DolarToday $:", format)
    euroFormat = response.json()["EUR"]["transferencia"]
    print("DolarToday €:", euroFormat)
    formatList = [format, euroFormat]
    # print(formatList)
dolartoday()
