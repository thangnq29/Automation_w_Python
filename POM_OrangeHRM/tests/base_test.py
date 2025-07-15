
import pytest
import allure
from selenium import webdriver
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_base_url())
        request.cls.driver = self.driver
        yield


        # Chụp màn nếu thất bại
        rep = getattr(request.node, "rep_call", None)
        if rep and rep.failed:
            try:
                screenshot = self.driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
                print("[Allure] Screenshot attached")
            except Exception as e:
                print(f"[Allure] Failed to attach screenshot: {e}")

        self.driver.quit()

