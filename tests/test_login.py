
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from time import sleep
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    def test_valid_login(self):
        username = self.driver.find_element(By.XPATH,"//input[@name='username']")
        password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        loginbt = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        username.send_keys("Admin")
        password.send_keys("admin123")
        loginbt.click()

        sleep(5)
        assert "dashboard" in self.driver.current_url.lower()
