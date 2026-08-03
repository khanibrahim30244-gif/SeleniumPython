import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/")

driver.find_element(By.LINK_TEXT, "Slider").click()

frame = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frame)

slider = driver.find_element(By.XPATH, "//*[@id='slider']/span")

actions = ActionChains(driver)
actions.drag_and_drop_by_offset(slider, 50, 0).perform()

time.sleep(3)
driver.close()