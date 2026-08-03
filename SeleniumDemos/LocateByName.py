import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com")

driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.NAME, "login-button").click()

time.sleep(2)
driver.close()