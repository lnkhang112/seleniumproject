import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest
from tests.test_login import TestLogin

@pytest.mark.usefixtures("setup")
class TestRecruitmentLogin:

    def test_recruitment(self):
        # Click vào menu Recruitment
        self.driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
        sleep(2)

        # Kiểm tra đã vào đúng trang Recruitment
        header = self.driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --visited']").click()
        assert header.is_displayed()