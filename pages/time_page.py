import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class TimePage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_time_page(self):
    # Click vào menu Time
        self.driver.find_element(By.XPATH, "//span[text()='Time']").click()
        sleep(2)

    # Xác thực đã vào trang Time
        assert "time" in self.driver.current_url.lower()