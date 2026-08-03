import pytest

from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.close()

def test_flipkart(driver):
    driver.get("https://www.flipkart.com/")
    title = driver.title
    print("Title is: " + title)

def test_lifestyle(driver):
    driver.get("https://www.lifestylestores.com/in/en")
    title = driver.title
    print("Title is: " + title)

def test_nykaa(driver):
    driver.get("https://www.nykaa.com/")
    title = driver.title
    print("Title is: " + title)