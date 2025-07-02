from pages.login_page import LoginPage
from tests.base_test import BaseTest

class TestLogin(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        assert self.driver.title == "OrangeHRM"
        login_page.do_login("Admin", "admin123")
