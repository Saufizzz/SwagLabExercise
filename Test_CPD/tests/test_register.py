import pytest

import Utilities.login_helper
from Utilities.BaseClass import BaseClass
from PageObjects.FimmSignUp import SignUp
from Utilities.login_helper import data_excel_Nric
from Utilities.login_helper import data_excel_Passport


class Test_Register(BaseClass):

    @pytest.mark.parametrize("NRIC, email", data_excel_Nric())
    def test_register_nric(self, NRIC, email):

        signup = SignUp(self.driver)
        signup.clickSignUpTab()
        self.WaitElementPresent(SignUp.NRIC_FIELD)
        signup.inputNRIC().send_keys(NRIC)
        signup.clickNextBtn()
        self.WaitElementPresent(SignUp.EMAIL_FIELD)
        signup.inputEmail().send_keys(email)
        signup.inputPassword().send_keys("@123QWea")
        signup.inputConfirmPassword().send_keys("@123QWea")
        signup.clickSubmitBtn()
        self.WaitElementPresent(SignUp.MSG)
        assert signup.displayMsg().is_displayed(), "try again"
        self.driver.refresh()

    @pytest.mark.parametrize("Passport, ExpiryDate, email", data_excel_Passport())
    def test_register_passport(self, Passport, ExpiryDate, email):
        signup = SignUp(self.driver)
        signup.clickSignUpTab()
        signup.clickNonMalaysianTab()
        self.WaitElementPresent(SignUp.PASSPORT_FIELD)
        signup.inputPASSPORT().send_keys(Passport)
        signup.inputPASSPORTEXPIRY().send_keys(ExpiryDate)
        signup.clickNextBtn()
        self.WaitElementPresent(SignUp.EMAIL_FIELD)
        signup.inputEmail().send_keys(email)
        signup.inputPassword().send_keys("@123QWea")
        signup.inputConfirmPassword().send_keys("@123QWea")
        signup.clickSubmitBtn()
        self.WaitElementPresent(SignUp.MSG)
        assert signup.displayMsg().is_displayed(), "try again"
        self.driver.refresh()




