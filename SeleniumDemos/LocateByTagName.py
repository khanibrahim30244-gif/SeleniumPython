from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.google.com/")

google_links = driver.find_elements(By.TAG_NAME, "a")

for links in google_links:
    all_links = links.text
    print(all_links)

driver.close()