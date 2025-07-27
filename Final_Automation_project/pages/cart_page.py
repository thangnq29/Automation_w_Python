
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = (By.ID, "checkout")
    
    def click_checkout(self):
        self.click(self.checkout_btn)
       
    