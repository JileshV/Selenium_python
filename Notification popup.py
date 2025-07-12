from selenium import webdriver
import time

ops = webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')

driver = webdriver.Chrome()
driver.get('https://whatmylocation.com/')
driver.maximize_window()
time.sleep(6)