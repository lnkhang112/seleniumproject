import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.webdriver.support.ui import Select

from time import sleep


class Vacancy(BasePage):
    ADD_BUTTON = (By.XPATH,'//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    ADD_VACANCY_NAME = (By.XPATH, '//label[contains(text(), "Vacancy Name")]/../../div//input')
    ADD_DESCRIPTION = (By.XPATH, '//textarea[@placeholder="Type description here"]')
    ADD_HIRING_MANAGER = (By.XPATH, '//input[@placeholder="Type for hints..."]')
    ADD_POSITION = (By.XPATH,'//label[contains(text(), "Number of Positions")]/../../div/input')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_add_button(self):
        # self.click(self.ADD_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON)).click()
        
    def add_vacancy_name(self,vacancy_name: str):
        # self.click(self.ADD_VACANCY_NAME)
        self.wait.until(EC.presence_of_element_located(self.ADD_VACANCY_NAME)).send_keys("vacancy name")
        
    # def add_description(self):
    #     self.click(self.ADD_DESCRIPTION)
    #     self.wait.until(EC.presence_of_element_located(self.ADD_DESCRIPTION)).click()
    def add_description(self):
        return self.driver.find_element(By.XPATH, '//textarea[@placeholder="Type description here"]')

        
    def add_hiring_manager(self):
        # self.click(self.ADD_HIRING_MANAGER)
        self.wait.until(EC.presence_of_element_located(self.ADD_HIRING_MANAGER)).click()
    def add_position(self):
        # self.click(self.ADD_POSITION)
        self.wait.until(EC.presence_of_element_located(self.ADD_POSITION)).click()
        
    def click_save_button(self):
        # self.click(self.SAVE_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SAVE_BUTTON)).click()

    def perform_complete_add_vacancy(self, vacancy_name: str, description: str, number_of_position: int):
        self.click_add_button()
        self.add_vacancy_name(vacancy_name)
        self.add_description().send_keys(description)


# Bước 4: Xác minh trang "Add Vacancy" hiển thị
    def verify_add_vacancy_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "addJobVacancy_name")) )

#  Nhập thông tin vacancy
     
    def fill_vacancy_form(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((self.ADD_DESCRIPTION))).send_keys("Automation Tester For Current Date")

        Select(self.driver.find_element(By.ID, 'class="oxd-select-text oxd-select-text--active"')).select_by_visible_text("Automation Tester")
        self.driver.find_element(By.ID, "addJobVacancy_description").send_keys("Automation Tester Is Running")

        hiring_manager = self.find_element(By.ID, "addJobVacancy_hiringManager")
        hiring_manager.clear()
        hiring_manager.send_keys("Admin")

        self.driver.find_element(By.ID, "addJobVacancy_noOfPositions").send_keys("1")

    # Bỏ chọn "Active"
        active_checkbox = self.driver.find_element(By.ID, "addJobVacancy_status")
        if active_checkbox.is_selected():
            active_checkbox.click()

    # Chọn "Publish in RSS Feed Web Page"
        rss_checkbox = self.driver.find_element(By.ID, "addJobVacancy_publishInRss")
        if not rss_checkbox.is_selected():
            rss_checkbox.click()


    


