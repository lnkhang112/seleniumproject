import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class InforPage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_infor_page(self):
    # Click vào menu My Info
        self.driver.find_element(By.XPATH, "//span[text()='My Info']").click()
        sleep(2)

    # Xác thực đã vào trang My Info
        assert "viewPersonalDetails" in self.driver.current_url.lower()