import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
location = os.getcwd()

serv_obj = Service("D:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

myWait = WebDriverWait(driver, 10, 2)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot(location+"/nopcommerce.jpg")
driver.get_screenshot_as_file(location+"/nopcommerce.jpg")
# driver.get_screenshot_as_png()

time.sleep(6)
driver.quit()