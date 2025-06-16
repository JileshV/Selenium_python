from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://money.rediff.com/gainers/bse/daily/groupa')
time.sleep(5)

# Locate all rows in the table (skip the first header row)
rows = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr")

print("Total companies found:", len(rows) - 1)

# Start from 2 because row 1 is usually the header
for x in range(1, len(rows) + 1):
    # Extract company name
    company_name_xpath = f"//*[@id='leftcontainer']/table/tbody/tr[{x}]/td[1]/a"
    company_name = driver.find_element(By.XPATH, company_name_xpath).text
    print("Company:", company_name)

    # Extract all columns in the current row
    row_data_xpath = f"//*[@id='leftcontainer']/table/tbody/tr[{x}]/td"
    columns = driver.find_elements(By.XPATH, row_data_xpath)

    for col in columns:
        print(col.text, end=' | ')
    print("\n" + "-" * 50)

driver.quit()
