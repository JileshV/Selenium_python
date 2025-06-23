import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
myWait = WebDriverWait(driver, 10,poll_frequency=2, ignored_exceptions=[Exception])

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()

dropDownElement = myWait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="input-country"]')))
# dropDownElement = driver.find_element(By.XPATH, '//select[@id="input-country"]')
dropDown = Select(dropDownElement)

dropDown.select_by_visible_text("New Zealand")

time.sleep(10)
driver.quit()