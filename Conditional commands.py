from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/Register')
# time.sleep(4)

searchBox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print(searchBox.is_displayed())
print(searchBox.is_enabled())

radioButton = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print(f"The Male radio button is selected: {radioButton.is_selected()}")

newsLetter = driver.find_element(By.XPATH, "//input[@id='Newsletter']")
print(f"The News letter option is selected: {newsLetter.is_selected()}")