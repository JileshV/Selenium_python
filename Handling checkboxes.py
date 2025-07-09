import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationintesting.com/selenium/testpage/')
driver.maximize_window()

# driver.find_element(By.XPATH, '//input[@id="checkbox1"]').click()

checkBoxes = driver.find_elements(By.XPATH, '//input[contains(@id,"checkbox")]')
print(len(checkBoxes))

for checkBox in checkBoxes:
    checkBox.click()

time.sleep(20)

driver.quit()