import os

from selenium.webdriver.common.by import By


class ProfPage:
    name = (By.XPATH,"//input[@name='name']")
    NRIC = (By.XPATH,"//div[@class='col-lg-5']//input[@id='icno']")
    Race = (By.XPATH,"//select[@id='race']")
    Nationality = (By.XPATH,"//select[@id='nationality']")
    DOB = (By.XPATH,"//input[@id='dob']")
    Age = (By.XPATH,"//input[@id='age']")
    Gender = (By.XPATH,"//select[@id='gender']")
    Add1 = (By.XPATH,"//input[@name='add1']")
    Add2 = (By.XPATH, "//input[@name='add2']")
    Add3 = (By.XPATH, "//input[@name='add3']")
    Postcode = (By.XPATH,"//input[@id='postcode']")
    City = (By.XPATH,"//select[@id='city_id']")
    State = (By.XPATH,"//select[@id='state_code']")
    AltPhone = (By.XPATH,"//input[@name='otherPhone']")
    SaveDraft = (By.XPATH,"//button[@id='save']")
    UpPhoto = (By.XPATH,"//input[@id='imgInp']")
    img = (By.XPATH,"//img[@id='blah']")
    Next = (By.XPATH,"//a[@href='#next']")

    RacErr = (By.XPATH,"//label[@id='race-error']")
    GendErr = (By.XPATH,"//label[@id='gender-error']")
    Add1Error = (By.XPATH,"//label[@id='add1-error']")
    Add2Error = (By.XPATH,"//label[@id='add2-error']")
    Add3Error = (By.XPATH,"//label[@id='add3-error']")
    PostCError = (By.XPATH,"//label[@id='postcode-error']")
    CityError = (By.XPATH,"//label[@id='city_id-error']")
    StateError = (By.XPATH,"//label[@id='city_id-error']")



    def __init__(self,driver):
        self.driver = driver

    def InsertName(self):
        return self.driver.find_element(*ProfPage.name)

    def InsetNRIC(self):
        return self.driver.find_element(*ProfPage.NRIC)

    def SelectRace(self):
        return self.driver.find_element(*ProfPage.Race)

    def SelectNationality(self):
        return self.driver.find_element(*ProfPage.Nationality)

    def SelectDOB(self):
        return self.driver.find_element(*ProfPage.DOB)

    def SelectGender(self):
        return self.driver.find_element(*ProfPage.Gender)

    def InsertAddress1(self):
        return self.driver.find_element(*ProfPage.Add1)

    def InsertAddress2(self):
        return self.driver.find_element(*ProfPage.Add2)

    def InsertAddress3(self):
        return self.driver.find_element(*ProfPage.Add3)

    def InsertPostcode(self):
        return  self.driver.find_element(*ProfPage.Postcode)

    def InsertState(self):
        return self.driver.find_element(*ProfPage.State)

    def InsertAltPhone(self):
        return self.driver.find_element(*ProfPage.AltPhone)

    def UploadPhoto(self):
        file_input = self.driver.find_element(*ProfPage.UpPhoto)
        #This tells Python to interpret the string as-is, without processing any escape sequences.
        file_path = os.path.abspath(r"C:\Users\muhds\Desktop\download (1).jpg")
        file_input.send_keys(file_path)

    def AssImg(self):
        return self.driver.find_element(*ProfPage.img)
    def CheckAge(self):
        age_field = self.driver.find_element(*ProfPage.Age)
        age_text = age_field.get_attribute("value")
        try:
            age = int(age_text)
        except ValueError:
            raise ValueError("Age input is not a valid integer.")

        if age < 21:
            assert False, "Age is less than 21."
        else:
            print("Age is higher than 21.")

    def Addr1Error(self):
        return self.driver.find_element(*ProfPage.Add1Error)

    def Addr2Error(self):
        return self.driver.find_element(*ProfPage.Add2Error)

    def Addr3Error(self):
        return self.driver.find_element(*ProfPage.Add3Error)

    def PostCodeErr(self):
        return self.driver.find_element(*ProfPage.PostCError)

    def CityErr(self):
        return self.driver.find_element(*ProfPage.CityError)

    def StateErr(self):
        return self.driver.find_element(*ProfPage.StateError)




    def GotoNext(self):
        self.driver.find_element(*ProfPage.Next).click()