import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    
    def click(self, element):
        element.click()

    def wait(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

    def dropdown(self, by_locator, visible_text):
        select = Select(self.driver.find_element(*by_locator))
        select.select_by_visible_text(visible_text)
