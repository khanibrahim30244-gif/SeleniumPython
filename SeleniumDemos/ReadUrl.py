from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.selenium.dev")

current_url = driver.current_url
print("Url is: ", current_url)

driver.quit()