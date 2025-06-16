from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(5)

#Full/Absolute Xpath *************
driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
#partial/Relative Xpath ************
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(4)
actual_title = driver.title
expected_title = 'OrangeHRM'
if actual_title == expected_title:
    print('Login test passed')
else:
    print('Login test failed')
driver.quit()

#or & and methods
#Example: //button[@id='submit_button' or @name='Submit']

#contains method
#Example: //button[contains(@id,'st')] for Start/stop button/element on webpage

#starts-with method
#Example: //*[starts-with(@id,'st')]

#text method
#Example: //a[text()='women'] to identify with the help of inner text of that particular element