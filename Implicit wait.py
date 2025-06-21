from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.implicitly_wait(20)      #This wait max 20 secs(Only when an element is not yet loaded)
driver.maximize_window()

driver.find_element(By.NAME, 'q').send_keys('Selenium')
driver.find_element(By.NAME, 'q').submit()      #Pressed Enter Key

driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()