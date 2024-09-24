from selenium.webdriver.common.by import By



class MainPage:
    CPDMenu = (By.XPATH, "//a[normalize-space()='Continuing Professional Development']")
    PostVet = (By.XPATH, "//a[normalize-space()='Post-Vetting']")
    AppStatus = (By.XPATH, "//a[normalize-space()='Application Status']")


    def __init__(self,driver):
        self.driver = driver

    def NavCPDMenu(self):
        self.driver.find_element(*MainPage.CPDMenu).click()

    def NavPostVet(self):
        self.driver.find_element(*MainPage.PostVet).click()

    def NavAppStatus(self):
        self.driver.find_element(*MainPage.AppStatus).click()