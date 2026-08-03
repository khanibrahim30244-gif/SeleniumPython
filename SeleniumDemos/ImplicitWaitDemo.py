from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()

current_url = driver.current_url
print(current_url)

if "dashboard" in current_url:
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()

driver.close()
