import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.com")

driver.find_element(By.PARTIAL_LINK_TEXT, "How").click()
print(driver.title)

time.sleep(3)

driver.back()
print(driver.title)
time.sleep(3)

driver.forward()
print(driver.title)
time.sleep(3)

driver.refresh()
time.sleep(3)

driver.close()
