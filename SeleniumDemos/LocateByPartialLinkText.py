from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://google.com")

driver.find_element(By.PARTIAL_LINK_TEXT,"Ad").click()

Title = driver.title
print(Title)

driver.close()