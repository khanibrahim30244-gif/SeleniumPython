from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/?m=1")

search_context = driver.find_element(By.ID, "shadow_host").shadow_root
search_context.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("ibrahim")