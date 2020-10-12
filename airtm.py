import requests
from bs4 import BeautifulSoup

# airtm

url = 'https://rates.airtm.com/'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
rates = soup.findAll('div', class_="text-6xl")
for rate in rates:
    rate.find('span', class_='rate--general')

print(rate.text)
