import requests
from bs4 import BeautifulSoup

url = "XXXXX"
response = requests.get(url)
print(dir(response))
html = response.text
soup = BeautifulSoup(html, 'html.parser')
#print(soup)