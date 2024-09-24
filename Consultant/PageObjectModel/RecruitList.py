from selenium.webdriver.common.by import By

from base.BaseClass import BaseClass


class RecruitPage(BaseClass):

    UploadFilesButton = (By.XPATH,"//button[normalize-space()='Upload Files']")
    SchemeSelection = (By.XPATH,"//select[@id='recruit_scheme']")
    ChooseFile = (By.XPATH,"//input[@id='recruit_file']")
    UploadButton = (By.XPATH,"//button[@id='upload_file']")
    OKButton = (By.XPATH,"//button[normalize-space()='Yes']")
    SuccessImage = (By.XPATH,"//div/i[@class='fa fa-check-circle']")
    RecruitText = (By.XPATH,"//a[@class='pr-3 active-1']")


    def __init__(self,driver):
        self.driver = driver

    def assertText(self):
        return self.driver.find_element(*RecruitPage.RecruitText)
    def ClickUploadFilesButton(self):
        self.WaitElementClickable(RecruitPage.UploadFilesButton)
        self.driver.find_element(*RecruitPage.UploadFilesButton).click()

    def SelectScheme(self,value,select_by='index'):
        self.WaitElementPresent(RecruitPage.SchemeSelection)
        self.select_option(RecruitPage.SchemeSelection,value, select_by)

    def ClickChooseFile(self):
        self.driver.find_element(*RecruitPage.ChooseFile).click()

    def ClickUploadButton(self):
        self.WaitElementClickable(RecruitPage.UploadButton)
        self.driver.find_element(*RecruitPage.UploadButton).click()

    def ClickOKButton(self):
        self.WaitElementClickable(RecruitPage.OKButton)
        self.driver.find_element(*RecruitPage.OKButton).click()

    def AssertImage(self):
        return self.driver.find_element(*RecruitPage.SuccessImage)

