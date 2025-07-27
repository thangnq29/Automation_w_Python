import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-features=PasswordLeakDetection")

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_base_url())
        request.cls.driver = self.driver
        yield
        self.driver.quit()
