# tests/test_login_integration.py
import allure
import pytest
from api.login_api import LoginAPI
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from tests.base_test import BaseTest


@allure.feature("Login API + UI Test")
class TestLoginAPIandUI(BaseTest):
    @allure.story("Login via API then open browser")
    def test_api_then_ui_login(self):
        api = LoginAPI()
        response = api.login(ConfigReader.get_username(), ConfigReader.get_password())
        
        assert response.status_code == 200, "API login failed"

        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())

        assert "Dashboard" in self.driver.title
