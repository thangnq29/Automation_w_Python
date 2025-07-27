from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import ConfigReader
from base.base_test import BaseTest
import allure
import pytest

@allure.feature("Checkout Process")
@allure.story("Successful Checkout with 3 Items")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test completing checkout with 3 products")
class TestCheckout(BaseTest):
    def test_checkout_process(self):
        login = LoginPage(self.driver)
        inventory = InventoryPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)

        login.do_login(ConfigReader.get_username(), ConfigReader.get_password())

        with allure.step("Add 3 products to cart"):
            inventory.add_n_products_to_cart(3)

        with allure.step("Click the shopping cart icon"):
            inventory.click_shopping_cart_icon()

        with allure.step("Click on Checkout button"):
            cart.click_checkout()

        with allure.step("Enter checkout information"):
            checkout.enter_checkout_info(
                ConfigReader.get_firstname(),
                ConfigReader.get_lastname(),
                ConfigReader.get_postal_code()  
            )

        with allure.step("Click Continue to proceed with checkout"):
            checkout.click_continue()

        with allure.step("Click Finish to place the order"):
            checkout.click_finish_btn()

        with allure.step("Verify full confirmation message after successful checkout"):
            assert ConfigReader.get_expected_message() == checkout.get_confirmation_message().strip(), f"\nExpected:\n{ConfigReader.get_expected_message()}\n\nActual:\n{checkout.get_confirmation_message()}"
