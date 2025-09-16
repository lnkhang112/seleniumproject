import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class DashBoard(BasePage):
    
    HEADER = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def verify_dashboard(self):
        header = self.wait.until(EC.presence_of_element_located(self.HEADER))
        return header.is_displayed
