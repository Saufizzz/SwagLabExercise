from selenium.webdriver.common.by import By
from pageObjectModel.productPage import ProductPage
from Utilities.BaseClass import BaseClass


class LoginPage:
    Username = (By.XPATH, "//input[@id='user-name']")
    Password = (By.XPATH, "//input[@id='password']")
    LoginBtn = (By.XPATH, "//input[@id='login-button']")
    ErrMsg = (By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match a')]")

    def __init__(self, driver):
        self.driver = driver

    def insertUsername(self, username):
        self.driver.find_element(*LoginPage.Username).send_keys(username)

    def insertPassword(self, password):
        self.driver.find_element(*LoginPage.Password).send_keys(password)

    def clickLoginBtn(self):
        self.driver.find_element(*LoginPage.LoginBtn).click()

    def errMsg(self):
        return self.driver.find_element(*LoginPage.ErrMsg)




