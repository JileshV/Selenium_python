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

image = myWait.until(ec.presence_of_element_located((By.ID, 'myImage')))
box = myWait.until(ec.presence_of_element_located((By.ID, 'targetDiv')))

act = ActionChains(driver)
act.drag_and_drop(image, box).perform()

time.sleep(5)