import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.maximize_window()

myWait = WebDriverWait(driver, 10, 2)

myWait.until(ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))).send_keys('Admin')
myWait.until(ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys('admin123')
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

myWait.until(ec.presence_of_element_located((By.XPATH, '//span[normalize-space()="Admin"]'))).click()
myWait.until(ec.presence_of_element_located((By.XPATH, '//span[normalize-space()="User Management"]'))).click()
myWait.until(ec.presence_of_element_located((By.XPATH, '//a[normalize-space()="Users"]'))).click()

myWait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]')))
rows = driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div')
# print(len(rows))
for row in range(1, len(rows)+1):
    status = driver.find_element(By.XPATH, f'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{row}]/div/div[5]/div').text
    # print(status)
    if status == 'Enabled':
        user = driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{row}]/div/div[2]/div').text
        print(user)

time.sleep(5)