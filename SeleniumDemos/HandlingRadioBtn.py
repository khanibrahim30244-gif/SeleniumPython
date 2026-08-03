from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://register.rediff.com/register/register.php?FormName=user_details")

radio_btn = driver.find_element(By.XPATH, "//input[@value='f']")

if not radio_btn.is_selected():
    radio_btn.click()
    print(radio_btn.is_selected())

else:
    print(radio_btn.is_selected())

driver.close()