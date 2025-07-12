from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

totalRows = driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr')
totalColumns = driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr[1]/th')

for row in range(1, len(totalRows)+1):
    for column in range(1, len(totalColumns)+1):
        if row == 1:
            data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{row}]/th[{column}]')
        else:
            data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{row}]/td[{column}]')
        print(data.text, ' | ', end='')
    print('\n')
