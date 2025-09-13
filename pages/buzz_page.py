import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class BuzzPage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_buzz_page(self):
    # Click vào menu Buzz
        self.driver.find_element(By.XPATH, "//span[text()='Buzz']").click()
        sleep(2)

    # Xác thực đã vào trang Buzz
        assert "buzz" in self.driver.current_url.lower()