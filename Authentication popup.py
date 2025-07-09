import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.maximize_window()
time.sleep(6)