import time
from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:\chromedriver-win64\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(8)
print(driver.title)
print(driver.current_url)
driver.close()