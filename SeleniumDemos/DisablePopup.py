from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
options.add_argument("--disable-notifications")

driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://register.rediff.com/register/register.php?FormName=user_details")

driver.find_element(By.PARTIAL_LINK_TEXT, "Rediff").click()