from selenium.webdriver.common.by import By


class LoginPage:
    username = (By.XPATH,"//input[@id='username']")
    Password = (By.XPATH,"//input[@id='Passwordss']")
    submit = (By.XPATH,"//button[@id='submit']")
    role = (By.XPATH,"//select[@id='role']")

    def __init__(self, driver):
        self.driver = driver

    def InsName(self,name):
        self.driver.find_element(*LoginPage.username).send_keys(name)

    def InsPassword(self,password):
        self.driver.find_element(*LoginPage.Password).send_keys(password)

    def clickSubmit(self):
        return self.driver.find_element(*LoginPage.submit).click()

    def SelectRole(self):
        return self.driver.find_element(*LoginPage.role)
