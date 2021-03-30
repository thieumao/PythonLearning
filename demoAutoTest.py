from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Declare browser
browser = webdriver.Chrome(executable_path="./chromedriver89")

# 2. Open Website
browser.get("https://www.facebook.com/")

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("YourEmail")

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("YourPassword")

txtPass.send_keys(Keys.ENTER)


# 3. Stop 5 seconds
sleep(5)

# 4. Close browser
browser.close()