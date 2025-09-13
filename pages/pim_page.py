import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from time import sleep

class PimPage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_pim_page(self):
    # Click vào menu PIM
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        sleep(2)

    # Xác thực đã vào trang PIM
        assert "pim" in self.driver.current_url.lower()