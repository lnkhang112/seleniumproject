import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class DerictoryPage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_directory_page(self):
    # Click vào menu Directory
        self.driver.find_element(By.XPATH, "//span[text()='Directory']").click()
        sleep(2)

    # Xác thực đã vào trang Directory
        assert "directory" in self.driver.current_url.lower()