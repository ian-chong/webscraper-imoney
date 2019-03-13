import requests
from bs4 import BeautifulSoup

r = requests.get('https://ringgitplus.com/en/business-loan/')
soup = BeautifulSoup(r.text, 'html.parser')

data_list=[]
cards = soup.find_all('tr', class_='loan')
for card in cards:
    bank_name = card.get('data-name')
    interest_rate = card.find('span', class_='data interest-rate').get_text()
    repayment = card.find('span', class_='data monthly-repayment').get_text()
    apply_link = card.find('a').get('href')
    new_data = {"bank name": bank_name, "interest rate": interest_rate, "repayment": repayment, "apply_link":apply_link}
    data_list.append(new_data)

breakpoint()
print(data_list)
