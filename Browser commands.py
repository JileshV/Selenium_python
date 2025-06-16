from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')

driver.maximize_window()
time.sleep(5)

driver.close() #Closes single browser window which the driver is focused

driver.quit() #Closes the all windows of the browser. Kills the driver