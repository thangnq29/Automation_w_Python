from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.complete_header_txt = (By.XPATH, "//h2[@class='complete-header']")
        self.confirm_txt = (By.XPATH, "//div[@class='complete-text']")

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)
    
    def enter_postal_code(self, postal_code):
        self.enter_text(self.postal_code, postal_code)

    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
    
    def click_continue(self):
        self.click(self.continue_btn)

    def click_finish_btn(self):
        self.click(self.finish_btn)

    def get_confirmation_message(self):
        title_text = self.get_text(self.complete_header_txt)
        body_text = self.get_text(self.confirm_txt)
        return f"{title_text} {body_text}"