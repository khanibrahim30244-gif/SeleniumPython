from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://www.selenium.dev/")