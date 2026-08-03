from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://google.com")

driver.find_element(By.LINK_TEXT, "About").click()

about_link = driver.title
print(about_link)

driver.close()