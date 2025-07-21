import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

from Alerts import alertPopUp

driver = webdriver.Chrome()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
myWait = WebDriverWait(driver, 10, 2)

button = driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')
act = ActionChains(driver)
act.context_click(button).perform()

quitButton = myWait.until(ec.presence_of_element_located((By.XPATH, '/html/body/ul/li[7]/span')))
act.move_to_element(quitButton).click().perform()

popUp = driver.switch_to.alert
popUp.accept()

time.sleep(6)