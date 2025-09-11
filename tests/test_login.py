from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest
from pages.login_page import LoginPage
# from pages.dashboard_page import TestDashBoard

@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    def test_valid_login(self):
        loginbtn = LoginPage(self.driver)
        loginbtn.login()
        
        # dashboardbtn = TestDashBoard(self.driver)
        # dashboardbtn.verify_dashboard_page()
        
        sleep(2)
        
        assert "dashboard" in self.driver.current_url.lower()