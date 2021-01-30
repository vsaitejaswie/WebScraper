from bs4 import BeautifulSoup 
from selenium import webdriver
import time

url = "https://www.naukri.com/"
url_suffix = input('enter the skill - ')
suffix_list = url_suffix.replace('.', ' ').split()

if url_suffix.startswith('.'):
    url = url + 'dot' + suffix_list[0] + '-' + 'jobs'
elif '.' in url_suffix:
    url = url + suffix_list[0] + '-' + 'dot' + '-' + suffix_list[1] + '-' + 'jobs'
else:
    for i in range(len(suffix_list)):
        url = url + suffix_list[i]  + '-' 
    url = url + 'jobs'
print("Connecting to:  " + url)
#url = "https://www.naukri.com/React-Dot-js-jobs"

driver = webdriver.Chrome(executable_path="/mnt/c/Users/sveeramr/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(url)

time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html5lib')

driver.close()
print("\n\nSuccess!\n-----------------------------------\n-----------------------------------")

articleTags = soup('article')

for tag in articleTags:
    experience = tag.find('li', class_ = "fleft grey-text br2 placeHolderLi experience")
    exp_period = experience.text.replace('-', ' ').split()
    #print(exp_period)
    if int(exp_period[0]) >= 5 and int(exp_period[1]) >= 5:
        job_title = tag.find('a', class_ = "title fw500 ellipsis")
        company_info = tag.find('a', class_ = "subTitle ellipsis fleft")
        print("Job-Title - " + job_title.text)
        print("Company - " + company_info.text)
        print("Experience - " + experience.text)
        print("Apply here - " + job_title.get('href'))
        print('\n\n')

#print(articleTags[0])