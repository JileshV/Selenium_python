import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

# Scroll py pixel
driver.execute_script('window.scrollBy(0,3000)', '')
value = driver.execute_script('return window.pageYOffset;')
print(value)

# Scroll upto an element
flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
driver.execute_script('arguments[0].scrollIntoView();', flag)
value = driver.execute_script('return window.pageYOffset;')
print(value)

# Scroll till end of the page
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
value = driver.execute_script('return window.pageYOffset;')
print(value)

# Scroll back to top
driver.execute_script('window.scrollBy(0, -document.body.scrollHeight)')

time.sleep(5)