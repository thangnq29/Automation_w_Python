from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_btn = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
        self.cart_btn = (By.XPATH, "//a[@class='shopping_cart_link']")

    def add_n_products_to_cart(self, n):
        buttons = self.find_elements(self.add_to_cart_btn)
        for btn in buttons[:n]:
            btn.click()
            
    def click_shopping_cart_icon(self):
        self.click(self.cart_btn)
        
