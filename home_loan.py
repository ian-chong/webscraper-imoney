import csv
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imoney.my/home-loan')
soup = BeautifulSoup(r.text, 'html.parser')

data_list=[]
cards = soup.find_all('div', class_="table__product")
for card in cards:
    bank_name = card.find_all('a')[2].get('data-value')
    interest_rate = card.find_all('span', class_='col-rate--item')[0].get_text()
    repayment = card.find_all('span', class_='col-rate--item')[2].get_text()
    apply_link = card.find('a').get('href')
    new_data = {"bank name": bank_name, "interest rate": interest_rate, "repayment": repayment, "apply link":apply_link}
    data_list.append(new_data)
with open ('home_loan.csv','w') as file:
    writer = csv.DictWriter(file, fieldnames = ["bank name", "interest rate", "repayment", "apply link"], delimiter = ';')
    writer.writeheader()
    for row in data_list:
        writer.writerow(row)

print(data_list)

