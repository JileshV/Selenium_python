from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://3dx.dsone.3ds.com/')
time.sleep(4)
driver.find_element(By.ID, 'username').send_keys('TRIGRAM')
driver.find_element(By.CLASS_NAME, 'uwa-input-submit').click()
time.sleep(2)
driver.find_element(By.ID, 'password').send_keys('PASSWORD')
driver.find_element(By.CLASS_NAME, 'uwa-input-submit').click()
time.sleep(15)
act_title = driver.title
expt_title = '3DS HOME - My Wall'

if act_title == expt_title:
    print('Successful Login to 3Dxperience platform')
else:
    print('Failed to Login to 3Dxperience platform')
time.sleep(3)
driver.quit()