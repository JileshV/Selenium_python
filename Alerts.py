import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

# Will pop up an alert
driver.find_element(By.XPATH, '//button[normalize-space()="Click for JS Prompt"]').click()
time.sleep(5)

alertPopUp = driver.switch_to.alert
print(alertPopUp.text)

alertPopUp.send_keys('Hello there!')
alertPopUp.accept()

# alertPopUp.dismiss()
time.sleep(5)