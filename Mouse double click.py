import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://artoftesting.com/samplesiteforselenium')
driver.maximize_window()

myWait = WebDriverWait(driver, 10, 2)

button = myWait.until(ec.presence_of_element_located((By.XPATH, '//button[@id="dblClkBtn"]')))
act = ActionChains(driver)
act.double_click(button).perform()

popUp = driver.switch_to.alert
popUp.accept()

time.sleep(6)