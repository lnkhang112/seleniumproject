import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_test import BaseTest
from base.base_page import BasePage


@pytest.mark.usefixtures("setup")
class Recruitment(BasePage):
    Recruitment = (By.XPATH, "//span[text()='Recruitment']")
    header = (By.XPATH, "//h5[text()='Candidates']")
    vacancies = (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item']")
    
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def test_recruitment(self):
    # Click vào menu Recruitment
        self.wait.until(EC.presence_of_element_located(self.Recruitment)).click()
    def verify_candidates_tab(self):
    # Xác thực đã vào trang Candidates
        self.wait.until(EC.presence_of_element_located(self.header)).click()

    def verify_vacancies_tab(self):
        self.click(self.vacancies)
    