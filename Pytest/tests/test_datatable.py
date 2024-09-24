import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
from Utilities.BaseClass import BaseClass


class TestDataTable(BaseClass):
    def test_login2(self):
        login = LoginPage(self)
        login.InsName().send_keys("sadmin")
        login.InsPassword().send_keys("WBTAWQ")
        login.clickSubmit()
        self.wait_element()
        self.SelectOption(login.SelectRole(),2)
        login.clickSubmit()
        self.wait_element()

    def test_admin_menu(self):
        mainpage = MainPage(self)
        mainpage.NavAdminMenu().click()
        self.driver.execute_script("arguments[0].scrollBy(0,500)", mainpage.SideBar())
        self.wait_element()
        mainpage.NavUsrMgmt().click()
        self.wait_element()
        self.driver.execute_script("window.scrollBy(0,1000)")
        expected_name = "shahrukhezudeen99@gmail.com"
        xpath_expected_text = (By.XPATH,"//td[2][normalize-space()='"+expected_name+"']")

        while True:
            try:
                #check if the expected name exist on the current page
                name_element = self.driver.find_element(By.XPATH,xpath_expected_text)
                if name_element.is_displayed():
                    print("Name Found", name_element.text)
                    break
            except NoSuchElementException:
                #if the name element is not found in the current page,scroll down to reveal more content
                self.driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
                #if the name element is not found on the current page,click on the next page
                next_page_link = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[contains(@class,'active')]/following::a[1]")))
                next_page_link.click()
                self.driver.find_element(By.XPATH,"//li[contains(@class,'active')]/following::a[1]")
                print("Next page link: ", next_page_link)#Add this line for debugging
                #Wait page to load
                time.sleep(5)





