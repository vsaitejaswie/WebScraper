import requests
from bs4 import BeautifulSoup

url = "https://www.naukri.com/react-dot-js-jobs-3"
response = requests.get(url)
#print(dir(response))
html = response.text
soup = BeautifulSoup(html, 'html5lib')
print(soup)