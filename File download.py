import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
fileLocation = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:\chromedriver-win64\chromedriver.exe")

    preferences = {"download.default_directory":fileLocation}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service = serv_obj, options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("D:\edgedriver_win64\msedgedriver.exe")

    preferences = {"download.default_directory": fileLocation}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("D:\geckodriver-v0.36.0-win64\geckodriver.exe")

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)   #0 for desktop, 1 for downloads folder & 2 for desired location
    ops.set_preference("browser.download.dir", fileLocation)

    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver

driver = edge_setup()
myWait = WebDriverWait(driver, 20, 2)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
# myWait.until(ec.presence_of_element_located((By.XPATH, "//a[@type='button']"))).click()
myWait.until(ec.presence_of_element_located((By.XPATH, "//textarea[@id='pdfbox']"))).send_keys("Hello Jilesh!")
myWait.until(ec.presence_of_element_located((By.XPATH, "//button[@id='createPdf']"))).click()
myWait.until(ec.presence_of_element_located((By.XPATH, "//a[@id='pdf-link-to-download']"))).click()

time.sleep(5)
driver.quit()