from selenium.webdriver.common.by import By

class PostVetPage:

    AddnewProgButton = (By.XPATH, "//a[normalize-space()='Add New Program']")
    ProgTitle = (By.XPATH, "//input[@id='title2']")
    ProceedBtn = (By.XPATH, "//button[@id='createApp']")

    def __init__(self,driver):
        self.driver = driver

    def ClickAddProgram(self):
        self.driver.find_element(*PostVetPage.AddnewProgButton).click()

    def InsertProgTitle(self):
        return self.driver.find_element(*PostVetPage.ProgTitle)

    def ClickProceedBtn(self):
        self.driver.find_element(*PostVetPage.ProceedBtn).click()
