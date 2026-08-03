import pytest

from selenium import webdriver

def test_selenium():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.selenium.dev/")

    Title = driver.title
    print(Title)

    driver.close()
