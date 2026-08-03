from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.selenium.dev/")

driver.save_screenshot("../screenshots/selenium_home.png")

driver.close()