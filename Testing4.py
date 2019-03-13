from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.get('https://www.imoney.my/car-loan?loantype=car+loan')
soup = BeautifulSoup(driver.page_source,"lxml")
for items in soup.select('.comparison-table'):
    docs = ' '.join([' '.join([item.text,' '.join(val.text.split())]) for item,val in zip(items.select(".event-name dt"),items.select(".event-name dd"))])
    location = ' '.join([' '.join(item.text.split()) for item in items.select(".event-location-type address")])
    print("Event_Info: {}\nEvent_Location: {}\n".format(docs,location))
driver.quit()