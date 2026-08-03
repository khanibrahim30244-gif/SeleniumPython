import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(3)

driver.close()