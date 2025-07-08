from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader
from selenium.webdriver.common.by import By
import allure

class TestLogin(BaseTest):

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        assert "dashboard" in self.driver.current_url