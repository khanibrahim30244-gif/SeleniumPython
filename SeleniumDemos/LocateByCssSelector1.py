from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

userName = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']")
userName.send_keys("standard_user")

userPass = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
userPass.send_keys("secret_sauce")

loginBtn = driver.find_element(By.CSS_SELECTOR, "input[name='login-button']")
loginBtn.click()