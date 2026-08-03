import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://register.rediff.com/register/register.php?FormName=user_details")

dropdown = driver.find_element(By.ID, "country")

country = Select(dropdown)
country.select_by_visible_text("Iran")

time.sleep(2)
country.select_by_value("107")
time.sleep(2)
country.select_by_index(5)

time.sleep(2)
driver.close()