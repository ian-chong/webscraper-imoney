from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.entrepreneur.com/article/296906')
soup = BeautifulSoup(site.text, 'lxml')

match3 = soup.find('a data-url-product-page')

match4 = soup.find_all('div', class_='art-v2-body')
print (match4)