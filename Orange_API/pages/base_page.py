from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from utils.config_reader import ConfigReader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.load_config().get("timeout", 20)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator):
        print(f"[Wait] Đang chờ element hiển thị: {locator}")
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"[ERROR] Timeout khi chờ element: {locator}")
            self.driver.save_screenshot("timeout_element.png")
            with open("debug_page.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise

    def wait_for_element_clickable(self, locator):
        print(f"[Wait] Đang chờ element có thể click: {locator}")
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def enter_text(self, locator, text, clear_first=True):
        element = self.wait_for_element_visible(locator)
        element.click()
        if clear_first:
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text
