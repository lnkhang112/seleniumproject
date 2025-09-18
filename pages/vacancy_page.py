import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class Vacancy(BasePage):
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    ADD_VACANCY_NAME = (By.XPATH, '//INPUT[@class="oxd-input oxd-input--active"]')
    ADD_DESCRIPTION = (By.XPATH, '//textarea[@placeholder="Type description here"]')
    ADD_HIRING_MANAGER = (By.XPATH, '(//div[@class="oxd-select-text-input"])[1]')
    ADD_POSITION = (By.XPATH, '(//div[@class="oxd-select-text-input"])[2]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_add_button(self):
        self.click(self.ADD_BUTTON)
        
    def add_vacancy_name(self):
        self.click(self.ADD_VACANCY_NAME)
        
    def add_description(self):
        self.click(self.ADD_DESCRIPTION)
        
    def add_hiring_manager(self):
        self.click(self.ADD_HIRING_MANAGER)
    
    def add_position(self):
        self.click(self.ADD_POSITION)
        
    def click_save_button(self):
        self.click(self.SAVE_BUTTON)