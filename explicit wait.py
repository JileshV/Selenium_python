from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()

myWait = WebDriverWait(driver, 20 ,poll_frequency=2, ignored_exceptions=[Exception])      #Creating an object for webdriverwait to wait for 20 sec

driver.find_element(By.NAME, 'q').send_keys('Selenium')
driver.find_element(By.NAME, 'q').submit()      #Pressed Enter Key

weblink = myWait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Selenium"]')))       #Waits until presence of element mentioned
weblink.click()

driver.quit()