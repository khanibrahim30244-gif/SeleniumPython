import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

expUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

@pytest.mark.parametrize("username,password",
    [
        ("admin", "admin123"),
        ("user1", "pass123"),
        ("admin", "admin123")
    ]
)

def test_login(username, password):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    actUrl = driver.current_url

    assert "dashboard" in actUrl, f"Expected Dashboard page, but title was: {expUrl}"

    if "dashboard" in driver.current_url:
        driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        print("Login Successful")
    else:
        print("Login Failed")

    driver.close()