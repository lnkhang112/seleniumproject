import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from base.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    
    username = (By.XPATH,"//input[@name='username']")
    password = (By.XPATH,"//input[@name='password']")
    loginbt = (By.XPATH,"//button[@type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self,user,password):
        self.get_element(self.username).send_keys(user)
        self.get_element(self.password).send_keys(password)
        self.click(self.loginbt)
        
        self.get_element
        

    
