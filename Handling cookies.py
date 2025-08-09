import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("D:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
cookies = driver.get_cookies()  #Gets all cookies
print(len(cookies))
for cookie in cookies:
    # print(cookie)
    print(cookie.get("name"))

driver.add_cookie({"name":"MyCookie", "value":"12345"})   #Adding a cookie
print(len(driver.get_cookies()))

driver.delete_cookie(".Nop.Customer")   #Deleting a cookie
print(len(driver.get_cookies()))

driver.delete_all_cookies()   #Deleting all cookies

time.sleep(5)