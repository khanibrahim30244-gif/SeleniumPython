from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.echotrak.com/Login.aspx?ReturnUrl=%2f")

driver.find_element(By.XPATH, "//input[@id='txtCustomerID']").send_keys("ibrahim123@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("ibrahim254")
driver.find_element(By.XPATH, "//input[@value='Login']").click()

print(driver.find_element(By.XPATH, "//*[contains(@id, 'lblMsg')]").text)
driver.close()