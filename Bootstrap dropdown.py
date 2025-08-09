import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service("D:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

myWait = WebDriverWait(driver, 10, 2)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
myWait.until(ec.presence_of_element_located((By.XPATH, "//span[@aria-label='Country']"))).click()
countries = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

for country in countries:
    if country.text == "China":
        country.click()
        break

time.sleep(8)