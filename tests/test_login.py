from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoard
from pages.recruitment_page import Recruitment
from pages.admin_page import AdminPage
from pages.pim_page import PimPage
from pages.leave_page import LeavePage
from pages.time_page import TimePage
from pages.infor_page import InforPage
from pages.performance_page import PerformancePage
from pages.directory_page import DerictoryPage
from pages.maintenance_page import MantenancePage
from pages.claim_page import ClaimPage
from pages.buzz_page import BuzzPage
from utils.config_reader import ConfigReader
@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):
    @pytest.mark.smoke
    def test_valid_login(self):
        
        getuser = ConfigReader.get_username(self.driver)
        getpass = ConfigReader.get_password(self.driver)
        login = LoginPage(self.driver)
        login.login(getuser, getpass)
        
        dashboardbtn = DashBoard(self.driver)
        dashboardbtn.verify_dashboard()
        
        
        recruitmentbtn = Recruitment(self.driver)
        recruitmentbtn.test_recruitment()

        # recruitment = Recruitment(self.driver)
        # recruitment.verify_candidates_tab()

        # admin_page = AdminPage(self.driver)
        # admin_page.go_to_admin_page()

        # pim_page = PimPage(self.driver)
        # pim_page.go_to_pim_page()

        # leave_page = LeavePage(self.driver)
        # leave_page.go_to_leave_page()

        # time_page = TimePage(self.driver)
        # time_page.go_to_time_page()

        # # infor_page = InforPage(self.driver)
        # # infor_page.go_to_infor_page()

        # performance_page = PerformancePage(self.driver)
        # performance_page.go_to_performance_page()

        # directory_page = DerictoryPage(self.driver)
        # directory_page.go_to_directory_page()

        # # maintenance_page = MantenancePage(self.driver)
        # # maintenance_page.go_to_maintenance_page()

        # claim_page = ClaimPage(self.driver)
        # claim_page.go_to_claim_page()

        # buzz_page = BuzzPage(self.driver)
        # buzz_page.go_to_buzz_page()
        
        # # assert "dashboard" in self.driver.current_url.lower()
        # # assert "recruitment" in self.driver.current_url.lower()
    
        