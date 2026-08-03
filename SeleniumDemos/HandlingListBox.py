from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

cars = Select(driver.find_element(By.ID, "multiselect1"))

all_cars = cars.options
print("---------------All Cars --------------------")
for car in all_cars:
    print(car.text)

if cars.is_multiple:
    cars.select_by_index(1)
    cars.select_by_index(3)

selected_Cars = cars.all_selected_options
print("-----------Selected Cars ------------")
for c in selected_Cars:
    print(c.text)

driver.quit()