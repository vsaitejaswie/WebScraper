#https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f#:~:text=Using%20urllib.&text=urlopen()%20to%20open%20a,to%20prevent%20from%20abnormal%20visit
#http://www.useragentstring.com/pages/useragentstring.php
# Program to access a https site with just urllib and 
# without importing ssl as shown in the lecture video

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
reg_url = "https://www.naukri.com/react-dot-js-jobs-3"
req = urllib.request.Request(url=reg_url, headers=headers) 
html = urllib.request.urlopen(req).read()
print(dir(html))
soup = BeautifulSoup(html, 'html.parser')
print(soup)