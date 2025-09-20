from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BaseTest:
    @pytest.fixture(scope="class", autouse=True) 
    def setup(self, request):
        Options = webdriver.ChromeOptions()
        Options.add_argument("--headless=new")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(2)
        request.cls.driver = driver
        yield
        driver.quit()