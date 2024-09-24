from selenium.webdriver.common.by import By

from base.BaseClass import BaseClass


class MainPage(BaseClass):


    #MainPage
    FIMMDisplay = (By.XPATH,"//img[@src='https://fimm-dev.zanko.com.my/assets/img/fimm/fimm-logo.png']")

    #CPD
    CPDMenu = (By.XPATH, "//a[normalize-space()='Continuing Professional Development']")
    PostVet = (By.XPATH, "//a[normalize-space()='Post-Vetting']")
    AppStatus = (By.XPATH, "//a[normalize-space()='Application Status']")



    #Consultant
    ConsultantMenu = (By.XPATH,"//a[normalize-space()='Consultant']")
    RecruitListSubmenu = (By.XPATH,"//a[normalize-space()='Recruit List']")


    def __init__(self,driver):
        self.driver = driver
    def ClickConsultantMenu(self):
        self.WaitElementPresent(MainPage.ConsultantMenu)
        self.driver.find_element(*MainPage.ConsultantMenu).click()

    def ClickRecruitListSubmenu(self):
        self.WaitElementPresent(MainPage.RecruitListSubmenu)
        self.driver.find_element(*MainPage.RecruitListSubmenu).click()



