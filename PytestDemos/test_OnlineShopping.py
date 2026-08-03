import pytest

from selenium import webdriver

@pytest.mark.order(3)
def test_flipkart():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.flipkart.com/")

    title = driver.title
    print("Title is: " + title)
    driver.close()

@pytest.mark.order(1)
def test_lifestyle():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.lifestylestores.com/in/en")

    title = driver.title
    print("Title is: " + title)
    driver.close()

@pytest.mark.order(2)
def test_nykaa():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.nykaa.com/")

    title = driver.title
    print("Title is: " + title)
    driver.close()