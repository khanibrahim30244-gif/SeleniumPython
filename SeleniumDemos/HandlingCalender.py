from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element(By.ID, "datepicker").click()

month = "Jan"
day = "9"

while month not in driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text:
    driver.find_element(
        By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span'
    ).click()

driver.find_element(By.XPATH, f"//a[text()='{day}']").click()

driver.quit()