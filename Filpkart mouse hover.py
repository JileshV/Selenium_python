import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://flipkart.com')
driver.maximize_window()

myWait = WebDriverWait(driver, 10, 2)

twoWheeler = myWait.until(ec.presence_of_element_located((By.XPATH, '//div[@aria-label="Two Wheelers"]')))

act = ActionChains(driver)
act.move_to_element(twoWheeler).perform()

electircVehicle = myWait.until(ec.presence_of_element_located((By.LINK_TEXT, 'Electric Vehicles')))
act.move_to_element(electircVehicle).click().perform()

time.sleep(6)