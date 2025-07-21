import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

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

# Mouse Hover
# act = webdriver.ActionChains(driver)
# act.move_to_element(userManagement).move_to_element(users).click().perform()

