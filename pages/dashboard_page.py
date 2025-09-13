import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class DashBoard():
    def __init__(self,driver):
        self.driver = driver

    def verify_dashboard(driver):
        try:
            driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").click()
        
        except Exception as e:
            print(f" Error verifying dashboard: {e}")
        return False
