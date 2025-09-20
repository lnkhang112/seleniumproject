from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope="class", autouse=True) 
    
    
    def setup(self, request):

        Options = webdriver.ChromeOptions()
        #Options.add_argument("--headless=new")
        driver = webdriver.Chrome()
        driver.maximize_window()
        base_url = ConfigReader.get_base_url()
        if base_url:
            driver.get(base_url)
        sleep(2)
        request.cls.driver = driver
        yield
        driver.quit()
        
