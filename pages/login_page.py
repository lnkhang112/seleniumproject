import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from time import sleep

class LoginPage():
    
    def __init__(self,driver):
        self.driver = driver
    
    def login(self):
        username = self.driver.find_element(By.XPATH,"//input[@name='username']")
        password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        loginbt = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        username.send_keys("Admin")
        password.send_keys("admin123")
        loginbt.click()
        sleep(5)
