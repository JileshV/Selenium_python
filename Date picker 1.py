import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/datepicker/')
driver.maximize_window()

driver.switch_to.frame(0)   #If only one frame, can write 0
# driver.find_element(By.XPATH, '//input[@id="datepicker"]').send_keys('07/02/2025')

year = '2025'
month = 'February'
day = '05'

driver.find_element(By.XPATH, '//input[@id="datepicker"]').click()
while True:
    yr = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-year"]').text
    mon = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-month"]').text
    if yr == year and mon == month:
        break
    else:
        driver.find_element(By.XPATH, '//a[@title="Prev"]').click()
driver.find_element(By.XPATH, '//a[normalize-space()="6"]').click()

time.sleep(6)