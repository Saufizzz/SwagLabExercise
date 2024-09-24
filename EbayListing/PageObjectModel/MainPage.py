from selenium.webdriver.common.by import By


class MainPage:
    Advanced = (By.XPATH, "//a[@title='Advanced Search']")

    def __init__(self, driver):
        self.driver = driver

    def clickAdvanced(self):
        self.driver.find_element(*MainPage.Advanced).click()
