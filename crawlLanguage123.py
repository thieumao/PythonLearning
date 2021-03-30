from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Declare browser
browser = webdriver.Chrome(executable_path="./chromedriver89")

# 2. Open Website
browser.get("https://language123.net/")

sleep(2)
''
test1 = browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div')
test1.click()
sleep(2)

part3 = browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[3]/div')
part3.click()
sleep(2)

divTitleList = browser.find_elements_by_xpath('//div[@dir="auto"]')
for div in divTitleList:
    print(div.text)

# 3. Stop 5 seconds
sleep(2)

# 4. Close browser
browser.close()