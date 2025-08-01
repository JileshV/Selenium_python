import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://text-compare.com/')
driver.maximize_window()

inputBox1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
inputBox2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
inputBox1.send_keys('Welcome to Selenium!')

act = ActionChains(driver)

# act.key_down(Keys.CONTROL)
# act.send_keys('a')
# act.key_up(Keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)
