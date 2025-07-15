
import pytest
import allure
from pages.myinfo_page import MyInfoPage
from utils.test_data_reader import TestDataReader
from tests.base_test import BaseTest
from tests.test_login import LoginPage
from utils.config_reader import ConfigReader


@allure.feature("My Info - Edit Employee")
class TestMyInfo(BaseTest):

    @allure.story("Edit employee name after login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_employee_name(self):  
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())

        myinfo_page = MyInfoPage(self.driver)
        myinfo_page.change_employee_name(TestDataReader.get_firstname(),TestDataReader.get_midname(),TestDataReader.get_lastname()
        )
