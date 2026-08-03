import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_About():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.google.com/")

    driver.find_element(By.LINK_TEXT, "About").click()
    Title = driver.title
    print("Title is: ", Title)

    driver.close()

def test_Gmail():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.google.com/")

    driver.find_element(By.LINK_TEXT, "Gmail").click()
    Title = driver.title
    print("Title is: ", Title)

    driver.close()

def test_Images():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.google.com/")

    driver.find_element(By.LINK_TEXT, "Images").click()
    Title = driver.title
    print("Title is: ", Title)

    driver.close()

def test_Ads():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.google.com/")

    driver.find_element(By.PARTIAL_LINK_TEXT, "Ad").click()
    Title = driver.title
    print("Title is: ", Title)

    driver.close()



