from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])

window_text = driver.find_element(By.TAG_NAME, "h3").text
print(window_text)

driver.quit()