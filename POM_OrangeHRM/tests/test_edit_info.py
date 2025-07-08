
# import pytest
# import allure
# from pages.myinfo_page import MyInfoPage
# from utils.test_data_reader import TestDataReader
# from tests.base_test import BaseTest

# @allure.feature("My Info - Edit Employee")
# class TestMyInfo(BaseTest):

#     @allure.story("Edit employee name after login")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_edit_employee_name(self, login):  # << sử dụng fixture login
#         myinfo_page = MyInfoPage(self.driver)
#         myinfo_page.change_employee_name(TestDataReader.get_firstname(),TestDataReader.get_midname(),TestDataReader.get_lastname()
#         )
