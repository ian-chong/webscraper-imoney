import csv
import requests
from bs4 import BeautifulSoup
data_list=[]
site = requests.get('https://www.imoney.my/small-business-loan')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
    questions = content.find_all(class_='comparison-table')
    for question in questions:
        topic = question.find(class_='question-hyperlink').get_text()
        url =   question.find(class_='question-hyperlink').get('href')
        views = question.find(class_='views').find(class_='mini-counts').find('span').get_text()
        answers = question.find(class_='status').find(class_='mini-counts').find('span').get_text()
        votes = question.find(class_='votes').find(class_='mini-counts').find('span').get_text()
        new_data = {"topic": topic, "url": url, "views": views, "answers":answers, "votes":votes}
        data_list.append(new_data)

print(data_list)