from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/upload")

file_path = "C:\\Users\\khani\\OneDrive\\Desktop\\Git.docx"

upload_file = driver.find_element(By.ID, "file-upload")
upload_file.send_keys(file_path)

driver.find_element(By.ID, "file-submit").click()

upload_text = driver.find_element(By.TAG_NAME, "h3")
print(upload_text.text)

driver.close()
