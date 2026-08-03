from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.selenium.dev")

Title = driver.title
print("Title is: " + Title)

driver.close()