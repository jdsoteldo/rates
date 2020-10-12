import requests
from bs4 import BeautifulSoup

# banco central de venezuela

url = 'http://www.bcv.org.ve/'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
rates = soup.findAll('div', class_="col-sm-6")
for rate in rates:
    rate.find('strong')

print(rate.text)
