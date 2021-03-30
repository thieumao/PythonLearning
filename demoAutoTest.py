from selenium import webdriver
from time import sleep

# 1. Declare browser
browser = webdriver.Chrome(executable_path="./chromedriver89")

# 2. Open Website
browser.get("https://www.facebook.com/")

# 3. Stop 5 seconds
sleep(5)

# 4. Close browser
browser.close()