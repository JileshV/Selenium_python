from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.snapdeal.com')
driver.maximize_window()
driver.get('https://www.amazon.in') #Opens in the same window replacing snapdeal.com
# time.sleep(2)
driver.back()   #Goes back to snapdeal
# time.sleep(2)
driver.forward()    #Comes forward to amazon
# time.sleep(2)
driver.refresh()    #Refreshes the page
# time.sleep(2)
driver.quit()