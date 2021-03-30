from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="./chromedriver89")
browser.get('https://www.forexfactory.com/calendar')
sleep(2)


divList = browser.find_elements_by_xpath('//span[@class="calendar__event-title"]')
for div in divList:
    print(div.text)

sleep(2)
browser.close()