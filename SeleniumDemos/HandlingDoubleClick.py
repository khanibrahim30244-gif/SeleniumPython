import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

doubleClick = driver.find_element(By.XPATH, "//button[@ondblclick = 'myFunction()']")

actions = ActionChains(driver)
actions.double_click(doubleClick).perform()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

alert.accept()

driver.close()