from base_test.basetest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
class TestLogin(BaseTest):
 
    def test_login_with_valid_credential(self):
   
        actual_title = self.driver.title
        expected_title = "OrangeHRM"
        assert actual_title == expected_title, f"Wrong title. Expected: {expected_title}, Got: {actual_title}"
 
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_input.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.TAG_NAME, "button").click()
   
    def test_login_with_invalid_credentials(self):
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_input.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin1234")
        self.driver.find_element(By.TAG_NAME, "button").click()
 
        error_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Invalid credentials']")))
        actual_error_message = error_element.text
        expected_error_message = "Invalid Username or Password"
        assert actual_error_message == expected_error_message, f"Wrong message. Expected: {expected_error_message}, Got: {actual_error_message}"
