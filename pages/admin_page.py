import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from time import sleep


class AdminPage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_admin_page(self):
    # Click vào menu Admin
        self.driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        sleep(2)

    # Xác thực đã vào trang Admin
        assert "admin" in self.driver.current_url.lower()