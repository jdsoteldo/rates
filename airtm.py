import requests
from bs4 import BeautifulSoup

# airtm


def airtm():
    airtmUrl = 'https://rates.airtm.com/'
    req = requests.get(airtmUrl)
    soup = BeautifulSoup(req.content, 'html.parser')
    rates = soup.findAll('div', class_="text-6xl")
    for rate in rates:
        rate.find('span', class_='rate--general')

    print("AirTM rate:", rate.text)

airtm()
