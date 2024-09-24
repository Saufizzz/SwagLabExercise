from selenium.webdriver.common.by import By


from selenium.webdriver.common.by import By

class SignUp:
    # Rename class-level variables to avoid conflicts
    SIGN_UP_TAB = (By.XPATH, "//a[normalize-space()='Sign Up']")
    NRIC_FIELD = (By.XPATH, "//input[@id='nric']")
    NEXT_BTN = (By.XPATH, "//button[@id='next']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='accemail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='pass']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@id='confirmPassword']")
    SUBMIT_BTN = (By.XPATH, "//button[@id='submits']")
    MSG = (By.XPATH, "//div[@class='alert alert-text alert-warning text-center']")
    NON_MALAYSIAN_TAB = (By.XPATH, "//label[normalize-space()='Non-Malaysian']")
    PASSPORT_FIELD = (By.XPATH, "//input[@id='passnumber']")
    PASSPORT_EXPIRY = (By.XPATH, "//input[@id='expdate']")

    def __init__(self, driver):
        self.driver = driver

    def clickSignUpTab(self):
        self.driver.find_element(*SignUp.SIGN_UP_TAB).click()

    def clickNonMalaysianTab(self):
        self.driver.find_element(*SignUp.NON_MALAYSIAN_TAB).click()

    def inputNRIC(self):
        return self.driver.find_element(*SignUp.NRIC_FIELD)

    def inputPASSPORT(self):
        return self.driver.find_element(*SignUp.PASSPORT_FIELD)

    def inputPASSPORTEXPIRY(self):
        return self.driver.find_element(*SignUp.PASSPORT_EXPIRY)

    def clickNextBtn(self):
        self.driver.find_element(*SignUp.NEXT_BTN).click()

    def inputEmail(self):
        return self.driver.find_element(*SignUp.EMAIL_FIELD)

    def inputPassword(self):
        return self.driver.find_element(*SignUp.PASSWORD_FIELD)

    def inputConfirmPassword(self):
        return self.driver.find_element(*SignUp.CONFIRM_PASSWORD_FIELD)

    def clickSubmitBtn(self):
        self.driver.find_element(*SignUp.SUBMIT_BTN).click()

    def displayMsg(self):
        return self.driver.find_element(*SignUp.MSG)

