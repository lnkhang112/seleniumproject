from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoard  
from pages.recruitment_page import Recruitment
from pages.vacancy_page import Vacancy

class TestVacancyPage(BaseTest):


    def test_vacancy(self):
        dashboard = DashBoard(self.driver)
        login = LoginPage(self.driver)
        recruitment = Recruitment(self.driver)
        vacancy = Recruitment(self.driver)
        vacancy_button = Vacancy(self.driver)
        add_button = Vacancy(self.driver)
        
        login.login("Admin", "admin123")
    
        dashboard.verify_dashboard()
        
        recruitment.test_recruitment()
        
        vacancy.verify_vacancies_tab()
        
        add_button.click_add_button()

        vacancy_button.fill_vacancy_form()



      