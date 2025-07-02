from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def enter_username(self, username):
        self.enter_text(self.username_input, username)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_login(self):
        self.click(self.login_btn)

