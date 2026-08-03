from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/?m=1")

pages = driver.find_elements(By.XPATH, "//ul[@id='pagination']/li/a")

for page in pages:
    page.click()

    rows = driver.find_elements(By.XPATH, "//*[@id='productTable']/tbody/tr")

    for row in rows:
        print(row.text)

driver.close()