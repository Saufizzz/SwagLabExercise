from selenium.webdriver.common.by import By



class MainPage:
    ConsMenu = (By.XPATH, "//a[normalize-space()='Consultant']")
    RegApplication = (By.XPATH, "//a[normalize-space()='Registration Application']")
    AppStatus = (By.XPATH, "//a[normalize-space()='Application Status']")
    AdminMenu = (By.XPATH,"//body/div@class='sidebar clearfix']/ul[@class='sidebar-panel nav']/li[12]/a[1]")
    sidebar_element = (By.XPATH,"//div[@class='sidebar clearfix']")
    UsrMngmnt = (By.XPATH,"//a[@href='https://fimm-dev.zanko.com.my/Admin/Usermgt']")

    def __init__(self,driver):
        self.driver = driver

    def NavConsMenu(self):
        self.driver.find_element(*MainPage.ConsMenu).click()

    def NavRegApplication(self):
        self.driver.find_element(*MainPage.RegApplication).click()

    def NavAppStatus(self):
        self.driver.find_element(*MainPage.AppStatus).click()

    def NavAdminMenu(self):
        return self.driver.find_element(self.AdminMenu)

    def SideBar(self):
        return self.driver.find_element(self.sidebar_element)

    def NavUsrMgmt(self):
        return self.driver.find_element(self.UsrMngmnt)

