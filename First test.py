# from webbrowser import Chrome

# import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(5)
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()
time.sleep(4)
actual_title = driver.title
expected_title = 'OrangeHRM'
if actual_title == expected_title:
    print('Login test passed')
else:
    print('Login test failed')
driver.quit()
