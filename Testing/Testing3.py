from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.imoney.my/car-loan')
soup = BeautifulSoup(site.text, 'lxml')

match3 = soup.find('a data-url-product-page')

match4 = soup.find_all('section data-v-65a81a20')
print (match4)