from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.com")

Title = driver.title
print(Title)

driver.close()