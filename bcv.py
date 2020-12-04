import requests
from bs4 import BeautifulSoup

# banco central de venezuela

bcvUrl = 'http://www.bcv.org.ve/'

def bcv():
    req = requests.get(bcvUrl)
    soup = BeautifulSoup(req.content, 'html.parser')
    rates = soup.findAll('div', class_="col-sm-6")
    for rate in rates:
        rate.find('strong')

    print("Banco Central de Venezuela:", rate.text.strip())

bcv()
