from selenium.webdriver.common.by import By
import os

class AcademicQualification:
    qual_level = (By.XPATH,"//select[@id='qualification_level']")
    add_button = (By.XPATH,"//button[normalize-space()='Add']")
    SPM_year = (By.XPATH,"//div[@class='col-lg-3']//select[@id='year']")
    SPM_School = (By.XPATH,"//div[@class='col-lg-6']//input[@name='Uname")
    Subject1 = (By.XPATH,"//tbody/tr[2]/td[1]/select[1]")
    Subject2 = (By.XPATH,"//tbody/tr[3]/td[1]/select[1]")
    Subject3 = (By.XPATH,"//tbody/tr[4]/td[1]/select[1]")
    Score1 = (By.XPATH,"//tbody/tr[2]/td[2]/select[1]")
    Score2 = (By.XPATH,"//tbody/tr[3]/td[2]/select[1]")
    Score3 = (By.XPATH,"//tbody/tr[3]/td[2]/select[1]")
    Del1 = (By.XPATH,"//tbody/tr[2]/td[3]/button[1]/i[1]")
    Del2 = (By.XPATH,"//tbody/tr[3]/td[3]/button[1]/i[1]")
    Del3 = (By.XPATH,"//tbody/tr[4]/td[3]/button[1]/i[1]")
    addfile = (By.XPATH,"//input[@id='attachment']")

    def __init__(self,driver):
        self.driver = driver

    def addAcademic(self):
        return self.driver.find_element(*AcademicQualification.qual_level)

    def addButton(self):
        self.driver.find_element(*AcademicQualification.add_button).click()