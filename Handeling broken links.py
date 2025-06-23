import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://deadlinkcity.com')
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0
for link in allLinks:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print(f'{url} is a broken link')
        count += 1

print(f'There are {count} number of broken links in this page')