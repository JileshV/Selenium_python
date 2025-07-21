import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@id="dob"]').click()

month = driver.find_element(By.XPATH, '//select[@aria-label="Select month"]')
Select(month).select_by_visible_text('May')
year = driver.find_element(By.XPATH, '//select[@aria-label="Select year"]')
Select(year).select_by_visible_text('1973')
driver.find_element(By.XPATH, '//a[normalize-space()="1"]').click()

time.sleep(6)