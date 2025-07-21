from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

totalRows = driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr')
totalColumns = driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr[1]/th')

print(f'Number of rows are {len(totalRows)}.')
print(f'Number of columns are {len(totalColumns)}.')

row = int(input('Enter thw row number: '))
column = int(input('Enter the column number: '))

if column == 1:
    data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr{[row]}/th{[column]}')
else:
    data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr{[row]}/td{[column]}')
print(data.text)
