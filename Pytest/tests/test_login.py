from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from PageObjects.MainPage import MainPage
from PageObjects.ProfilePage import ProfPage
from PageObjects.RegistrationPage import RegPage
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage

class TestLogin(BaseClass):
    def test_login1(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.InsName()
        loginpage.InsPassword()
        loginpage.clickSubmit()
        self.driver.implicitly_wait(10)
        #only for selecting role
        #self.SelectOption(loginpage.SelectRole(),2)
        #loginpage.clickSubmit()
        self.driver.implicitly_wait(30)
        FIMM = self.driver.find_element(By.XPATH,"//img[@src='https://fimm-dev.zanko.com.my/assets/images/fimm/fimm-logo.png']").is_displayed()
        assert FIMM, "image error not found"

    def test_register(self):
        mainPage = MainPage(self.driver)
        mainPage.NavConsMenu()
        self.driver.implicitly_wait(20)
        mainPage.NavRegApplication()
        assert self.driver.find_element(By.XPATH,"//h4[normalize-space()='Consultant Registration']").is_displayed(), "Wrong Page"

    def test_upload_photo(self):
        profPage = ProfPage(self.driver)
        assert profPage.AssImg().is_displayed(),"No image is displayed"

    def test_profile_error(self):
        profPage = ProfPage(self.driver)
        self.driver.execute_script("window.scrollBy(0,1000)","")
        profPage.GotoNext()
        self.driver.implicitly_wait(30)
        try:
            profPage.CheckAge()
        except AssertionError as e:
            print(e) #handle assertion error here if age is less than 21
        assert profPage.Addr1Error().is_displayed(),"Error not found"
        assert profPage.PostCodeErr().is_displayed(),"Error not found"
        assert profPage.CityErr().is_displayed(), "Error not found"
        assert profPage.StateErr().is_displayed(), "Error not found"

    def test_insertValue(self):
        profPage = ProfPage(self.driver)
        self.SelectOption(profPage.SelectRace(),1)
        # Convert the WebElement representing the gender dropdown to a Select object
        select_race = Select(profPage.SelectRace())
        # Get the first selected option from the dropdown
        selected_race = select_race.first_selected_option.text

        self.SelectOption(profPage.SelectGender(),1)
        # Convert the WebElement representing the gender dropdown to a Select object
        select_gender = Select(profPage.SelectGender())
        # Verify that the selected option is "Male"
        assert selected_race == "MALAY", f"Expected 'MALAY', but found '{selected_race}'"

        # Get the first selected option from the dropdown
        selected_gender = select_gender.first_selected_option.text

        # Verify that the selected option is "Male"
        assert selected_gender == "MALE", f"Expected 'MALE', but found '{selected_gender}'"
        profPage.InsertAddress1().send_keys("No.19 Persiaran Teratai 5")
        profPage.InsertAddress2().send_keys("Jalan Teratai")
        profPage.InsertAddress3().send_keys("Sungai Ramal Dalam")
        profPage.InsertPostcode().send_keys("43000")
        self.driver.execute_script("window.scrollBy(0,1000)","")
        profPage.GotoNext()









