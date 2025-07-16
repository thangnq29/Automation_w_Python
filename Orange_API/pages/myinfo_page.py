from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class MyInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.myinfo = (By.XPATH,"//a[@href='/web/index.php/pim/viewMyDetails']")
        self.enter_new_first_name = (By.XPATH, "//input[@name='firstName']")
        self.enter_new_middle_name = (By.XPATH, "//input[@name='middleName']")
        self.enter_new_last_name = (By.XPATH,"//input[@name='lastName']")
        self.submit_btn = (By.XPATH,"(//button[@type='submit'])[1]")

    def navigate_to_myinfo(self):
        self.click(self.myinfo)

    def change_firstname(self,firstname):
        self.enter_text(self.enter_new_first_name, firstname,)
    
    def change_middlename(self,middlename):
        self.enter_text(self.enter_new_middle_name, middlename)

    def change_lastname(self,lastname):
        self.enter_text(self.enter_new_last_name, lastname)

    def click_submit_btn(self):
        self.click(self.submit_btn)

    def change_employee_name(self, firstname, middlename, lastname):
        self.navigate_to_myinfo()
        self.wait_for_element_visible(self.enter_new_first_name)  
        self.change_firstname(firstname)
        self.change_middlename(middlename)
        self.change_lastname(lastname)
        self.click_submit_btn()