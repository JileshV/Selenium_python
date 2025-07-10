import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.maximize_window()
myWait = WebDriverWait(driver, 10, 2)

# Window IDs are dynamic, it changes when reopened the window multiple times
# driverId = driver.current_window_handle     Gets window ID of current active window

webLink = myWait.until(ec.presence_of_element_located((By.LINK_TEXT, 'OrangeHRM, Inc')))
webLink.click()

windowIDs = driver.window_handles
parentWindow = windowIDs[0]
childWindow = windowIDs[1]

driver.switch_to.window(windowIDs[1])
time.sleep(5)