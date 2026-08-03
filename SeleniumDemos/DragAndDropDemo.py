import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/")

driver.find_element(By.LINK_TEXT, "Droppable").click()

frame = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frame)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(2)
driver.close()