from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, 'input#small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')
driver.find_element(By.CLASS_NAME, 'search-box-button').click()
time.sleep(20)

# driver.find_element(By.LINK_TEXT, 'Register').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Regis').click()
# driver.find_element(By.CSS_SELECTOR, 'button#product-box-add-to-cart-button').click()
# time.sleep(50)

# sliders = driver.find_elements(By.CLASS_NAME, '')
# print(sliders)