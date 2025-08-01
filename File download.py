import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def chrome_setup():
    driver = webdriver.Chrome()
    return driver

# def edge_setup():
#     driver = webdriver.Edge()
#     return driver

# def firefox_setup():
#     driver = webdriver.firefox
#     return driver


driver = chrome_setup()
myWait = WebDriverWait(driver, 20, 2)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
myWait.until(ec.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[5]/a[1]"))).click()

time.sleep(5)