from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
# time.sleep(4)

pageTitle = driver.title
print(pageTitle)

currentUrl = driver.current_url
print(currentUrl)

