from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkbox = driver.find_element(By.ID, "checkBoxOption2")

if not checkbox.is_selected():
    checkbox.click()
    print(checkbox.is_selected())
else:
    print(checkbox.is_selected())

driver.close()