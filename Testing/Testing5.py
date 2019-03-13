import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.imoney.my/small-business-loan')
if site.status_code is 200:
    soup = BeautifulSoup(site.content, 'html.parser')
    match = soup.findAll ('div')

print(match)
