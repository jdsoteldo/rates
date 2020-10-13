import requests
from bs4 import BeautifulSoup

url = 'https://monitordolarvenezuela.com/'

def monitor():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    rates = soup.find(id="Costo")
    print(rates.text)

monitor()
