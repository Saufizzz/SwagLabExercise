from selenium.webdriver.common.by import By
from base.BaseClass import BaseClass

class LoginPage(BaseClass):
    username = (By.XPATH,"//input[@id='username']")
    Password = (By.XPATH,"//input[@id='Passwordss']")
    submit = (By.XPATH,"//button[@id='submit']")
    role = (By.XPATH,"//select[@id='role']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.Password).send_keys(password)

    def clickSubmit(self):
        return self.driver.find_element(*LoginPage.submit).click()

    def select_role(self, role, select_by='index'):
        self.select_option(LoginPage.role, role, select_by)
