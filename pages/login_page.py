import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from base.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self):
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        loginbt = self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        
        # self.get_element(self.username)
        sleep(5)
