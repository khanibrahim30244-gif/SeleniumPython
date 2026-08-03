from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()

menu = driver.find_elements(By.XPATH, "//ul[@class = 'oxd-main-menu']/li/a")
for menuItem in menu:
    print(menuItem.text)

driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
driver.find_element(By.LINK_TEXT, "Logout").click()

driver.close()