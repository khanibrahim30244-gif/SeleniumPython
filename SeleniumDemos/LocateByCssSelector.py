from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://login.salesforce.com/?locale=in")

driver.find_element(By.CSS_SELECTOR,"#username").send_keys("ibrahim")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("ibrahim158")
driver.find_element(By.CSS_SELECTOR, ".password").clear()
