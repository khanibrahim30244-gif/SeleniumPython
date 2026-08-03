from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Switch into iframe
wait.until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "courses-iframe"))
)

# Click Courses inside the iframe
wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Courses"))
).click()

# The linked Courses page has an h1, not the expected h2 text
heading = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)

print(heading.text)

driver.quit()