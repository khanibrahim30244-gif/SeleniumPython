from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//table/thead/tr/th/span[text() = 'Veg/fruit name']").click()
veggieText = driver.find_elements(By.XPATH, "//tr/td[1]")

for veg in veggieText:
    browserSortedVeggies.append(veg.text)

originalBrowserSortedList = browserSortedVeggies.copy()

browserSortedVeggies.sort()
print(browserSortedVeggies)
assert browserSortedVeggies == originalBrowserSortedList

driver.close()