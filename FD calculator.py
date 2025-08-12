import openpyxl
import ExcelModule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

servObj = Service("D:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(8)

file = "D:\FD_calc_data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = "Sheet1"
principal = ExcelModule.readData(file, sheet, 2, 1)
roi = ExcelModule.readData(file, sheet, 2, 2)
period = ExcelModule.readData(file, sheet, 2, 3)

driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principal)
driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(roi)
driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period)
tenurePeriod = driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")
tenure = Select(tenurePeriod)
tenure.select_by_visible_text("year(s)")
frequencyDropDown = driver.find_element(By.XPATH, "//select[@id='frequency']")
frequency = Select(frequencyDropDown)
frequency.select_by_visible_text("Compounded Yearly")
driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()

maturityValue = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text
print(f"The Maturity value will be {maturityValue}")

ExcelModule.writeData(file, sheet, maturityValue, 2, 4)

time.sleep(6)