import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, 500)")
time.sleep(3)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)

driver.execute_script("window.scrollBy(0, 0)")
time.sleep(3)

driver.quit()