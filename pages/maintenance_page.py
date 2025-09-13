import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class MantenancePage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_maintenance_page(self):
    # Click vào menu Maintenance
        self.driver.find_element(By.XPATH, "//span[text()='Maintenance']").click()
        sleep(2)

    # Xác thực đã vào trang Maintenance
        assert "maintenance" in self.driver.current_url.lower()