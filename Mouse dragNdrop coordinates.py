import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://simeydotme.github.io/jQuery-ui-Slider-Pips/')
driver.maximize_window()

myWait = WebDriverWait(driver, 10, 2)

# time.sleep(10)
leftSlider = myWait.until(ec.presence_of_element_located((By.XPATH, "/html/body/section/section/section[7]/section[7]/div[2]/div[1]/div/span[1]")))
rightSlider = myWait.until(ec.presence_of_element_located((By.XPATH, "/html/body/section/section/section[7]/section[7]/div[2]/div[1]/div/span[2]")))

# print(leftSlider.location)  #{'x': 647, 'y': 10444}
# print(rightSlider.location)  #{'x': 1524, 'y': 10444}

act = ActionChains(driver)
act.drag_and_drop_by_offset(leftSlider, -100, 0).perform()
act.drag_and_drop_by_offset(rightSlider, 100, 0).perform()

time.sleep(6)   #132 & 868
