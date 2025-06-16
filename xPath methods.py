from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://money.rediff.com/gainers/bse/daily/groupa')
# driver.maximize_window()
time.sleep(5)

company_list = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr")
print(len(company_list))
for x in range (1, len(company_list)):
    company_data = driver.find_elements(By.XPATH, f"//*[@id='leftcontainer']/table/tbody/tr[{x}]/td")
    for i in range(1, len(company_data)):
        text_msg = driver.find_element(By.XPATH, f"//*[@id='leftcontainer']/table/tbody/tr[{x}]/td[{i}]").text
        print(text_msg)
    print("")


# time.sleep(4)