from selenium.webdriver.common.by import By

class RegPage:
    registration_application = (By.XPATH,"//a[normalize-space()='Consultant']")
    nav_to_register = (By.XPATH,"//a[normalize-space()='Registration Application']")

    def __init__(self, driver):
        self.driver = driver

    def NavReg(self):
        #self.driver.find_element(By.XPATH,"//a[normalize-space()='Consultant']")
        #* will deserialize the tuple and the code will be read as tuple style
        self.driver.find_element(*RegPage.registration_application).click()
        self.driver.implicitly_wait(10)
        #self.driver.find_element(By.XPATH,"//a[normalize-space()='Registration Application']")
        self.driver.find_element(*RegPage.nav_to_register).click()