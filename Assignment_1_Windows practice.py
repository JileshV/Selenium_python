import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
myWait = WebDriverWait(driver, 10, 2)

myWait.until(ec.presence_of_element_located((By.XPATH, '//button[@id="confirmBtn"]'))).click()
popUp = driver.switch_to.alert
popUp.accept()

myWait.until(ec.presence_of_element_located((By.CLASS_NAME, 'wikipedia-search-input'))).send_keys('selenium')
myWait.until(ec.presence_of_element_located((By.CLASS_NAME, 'wikipedia-search-button'))).click()
searchResults = myWait.until(ec.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/div[2]/div')))
print(len(searchResults))
for result in range(1, len(searchResults)+1):
    driver.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/div[2]/div[{result}]/a').click()
time.sleep(8)

windows = driver.window_handles
for window in windows:
    driver.switch_to.window(window)
    if driver.title != 'Automation Testing Practice':
        print(driver.title)

time.sleep(3)
