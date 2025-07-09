import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()

driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()

frame1 = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(frame1)
frame2 = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('Jilesh')

# driver.switch_to.frame('Frame Name')  To switch to a particular frame
# driver.switch_to.default_content()    To switch back to main page

time.sleep(5)