import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class PerformancePage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_performance_page(self):
    # Click vào menu Performance
        self.driver.find_element(By.XPATH, "//span[text()='Performance']").click()
        sleep(2)

    # Xác thực đã vào trang Performance
        assert "performance" in self.driver.current_url.lower()