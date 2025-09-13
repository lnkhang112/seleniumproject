import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from time import sleep

class LeavePage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_leave_page(self):
    # Click vào menu Leave
        self.driver.find_element(By.XPATH, "//span[text()='Leave']").click()
        sleep(2)

    # Xác thực đã vào trang Leave
        assert "leave" in self.driver.current_url.lower()