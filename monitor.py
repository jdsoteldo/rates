import requests
from bs4 import BeautifulSoup

# monitor dolar venezuela

monitorUrl = 'https://monitordolarvenezuela.com/'

def monitor():
    req = requests.get(monitorUrl)
    soup = BeautifulSoup(req.content, 'html.parser')
    rates = soup.find(id="Costo")
    print("Monitor dolar Venezuela:", rates.text)

monitor()
