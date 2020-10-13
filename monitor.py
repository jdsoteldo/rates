import requests
from bs4 import BeautifulSoup

# monitor dolar venezuela

monitorUrl = 'https://monitordolarvenezuela.com/'

def monitor():
    req = requests.get(monitorUrl)
    soup = BeautifulSoup(req.content, 'html.parser')
    rates = soup.find(id="Costo")
    # get rid of white space and divides the string into a list
    prates = rates.text.split()
    # print only the first element, which is the amount
    print("Monitor dolar Venezuela:", prates)

monitor()
