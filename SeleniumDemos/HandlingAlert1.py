from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("ibrahim")
driver.find_element(By.ID, "confirmbtn").click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

# alert.accept()
alert.dismiss()

driver.close()