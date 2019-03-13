import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imoney.my/personal-loan')
soup = BeautifulSoup(r.text, 'html.parser')

data_list=[]
cards = soup.find_all('div', class_='table__product')
for card in cards:
    bank_name = card.get('data-bank')
    interest_rate = card.find_all('div', class_='col-rate--item')[0].get_text()
    repayment = card.find_all('div', class_='col-rate--item')[1].get_text()
    apply_link = card.find('a').get('href')
    new_data = {"bank name": bank_name, "interest rate": interest_rate, "repayment": repayment, "apply_link":apply_link}
    data_list.append(new_data)

breakpoint()
print(data_list)
