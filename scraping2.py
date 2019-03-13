from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\ian\\Desktop\\Testing\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.imoney.my/personal-loan")
assert "Python" in driver.title
elem = driver.find_elements_by_class_name("div")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()