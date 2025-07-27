from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from base.base_test import BaseTest
import allure
import pytest


@allure.feature("Login Functionality")
@allure.story("Valid Login Test")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin(BaseTest):
    def test_login_success(self):
        login = LoginPage(self.driver)

        with allure.step("Perform login with valid credentials"):
            login.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        
        with allure.step("Verify redirection to Inventory page"):
            assert ConfigReader.get_expected_url()== self.driver.current_url, f"Expected URL: {ConfigReader.get_expected_url()}, but got: {self.driver.current_url}"