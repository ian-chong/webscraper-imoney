import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imoney.my/car-loan')
soup = BeautifulSoup(r.text, 'html.parser')

data_list=[]
cards = soup.find_all('div', class_="columns list-item__info is-mobile is-multiline has-text-centered-mobile")
for card in cards:
    bank_name = card.find('a').get_text()
    interest_rate = card.find_all('b')[0].get_text()
    repayment = card.find_all('b')[1].get_text()
    apply_link = card.find('a').get('href')
    new_data = {"bank name": bank_name, "interest rate": interest_rate, "repayment": repayment, "apply_link":apply_link}
    data_list.append(new_data)

print(data_list)

