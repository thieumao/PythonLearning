import requests
from bs4 import BeautifulSoup

response = requests.get("https://language123.net/")
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

titles = soup.findAll('h3', class_='title-news')
print(titles)