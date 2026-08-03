import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/upload-download-test/")

driver.find_element(By.ID, "downloadButton").click()

time.sleep(3)

driver.close()