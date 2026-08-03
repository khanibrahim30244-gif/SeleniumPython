import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

rightClickBtn = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

actions = ActionChains(driver)
actions.context_click(rightClickBtn).perform()

time.sleep(3)
driver.close()