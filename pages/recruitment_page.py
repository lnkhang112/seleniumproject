import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class Recruitment():
    def __init__(self,driver):
        self.driver = driver

    def test_recruitment(self):
    # Click vào menu Recruitment
        self.driver.find_element(By.XPATH, "//span[text()='Recruitment']").click()
        sleep(2)

    def verify_candidates_tab(self):
    # Xác thực đã vào trang Candidates
        header = self.driver.find_element(By.XPATH, "//h5[text()='Candidates']")
        assert header.is_displayed()

    # def verify_vacancies_tab(self):
    # # Click vào tab Vacancies
    #     self.driver.find_element(By.XPATH, '//a[@class='oxd-topbar-body-nav-tab-item'"]').click()

    # # Xác thực đã vào đúng tab
    #     header = self.driver.find_element(By.XPATH, "//h5[text()='Vacancies']")
    #     assert header.is_displayed()