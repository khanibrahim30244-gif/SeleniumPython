from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://istqb.in/")

spMenu = driver.find_element(By.LINK_TEXT, "SPECIALIST")

action = ActionChains(driver)
action.move_to_element(spMenu).perform()

menus = driver.find_elements(By.XPATH,"//ul[@class='sp-dropdown-items']/li/a")
for menu in menus:
    print(menu.text)

driver.close()