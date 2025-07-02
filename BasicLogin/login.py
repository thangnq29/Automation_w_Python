import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = self.driver
        request.cls.wait = self.wait
        yield
        self.driver.quit()

@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    def test_loginWithValidCredential(self):
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_input.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

        actual_title = self.driver.title
        expected_title = "OrangeHRM"
        assert actual_title == expected_title, f"Wrong title. Expected: {expected_title}, Got: {actual_title}" 