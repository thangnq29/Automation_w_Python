
import pytest
import allure
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.test_data_reader import TestDataReader
from tests.base_test import BaseTest
from pages.myinfo_page import MyInfoPage


@allure.feature("Login and Edit Employee Info")
class TestLogin(BaseTest):

    @allure.story("Valid Login and Edit Info")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        assert "dashboard" in self.driver.current_url

        myinfo_page = MyInfoPage(self.driver)
        myinfo_page.change_employee_name(TestDataReader.get_firstname(),TestDataReader.get_midname(),TestDataReader.get_lastname())
