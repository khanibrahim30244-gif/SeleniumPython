from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://google.com")

google_search = driver.find_element(By.CLASS_NAME, "gLFyf")
google_search.send_keys("selenium")
google_search.send_keys(Keys.RETURN)