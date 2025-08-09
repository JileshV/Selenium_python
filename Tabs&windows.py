import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service("D:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

myWait = WebDriverWait(driver, 10, 2)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# regLink = Keys.CONTROL+Keys.RETURN  #To open the link in a new tab
# driver.find_element(By.LINK_TEXT, "Register").send_keys(regLink)
# windowIDs = driver.window_handles
# driver.switch_to.window(windowIDs[1])

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window() #For launching new tab
# driver.get("https://www.orangehrm.com/")

driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")   #For launching new window
driver.get("https://www.orangehrm.com/")

time.sleep(6)
driver.quit()