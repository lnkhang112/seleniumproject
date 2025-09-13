import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest

class ClaimPage():
    def __init__(self,driver):
        self.driver = driver

    def go_to_claim_page(self):
    # Click vào menu Maintenance
        self.driver.find_element(By.XPATH, "//span[text()='Claim']").click()
        sleep(2)

    # Xác thực đã vào trang Maintenance
        assert "claim" in self.driver.current_url.lower()