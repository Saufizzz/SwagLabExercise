import os
import tempfile
import pytest
import time

from selenium.common import StaleElementReferenceException

from PageObjectModel.LoginPage import LoginPage
from PageObjectModel.MainPage import MainPage
from PageObjectModel.RecruitList import RecruitPage
from base.BaseClass import BaseClass
from utilities.Edit_excel_helper import load_excel_file, modify_excel_file
from utilities.cookies_helper import CookiesHelper  # Assuming your helper class is named CookiesHelper

class TestLogin(BaseClass):
    # Parameterize the test function with different sets of data

    @pytest.mark.parametrize("modifications", [
        [(2, 2, "990909090020")],  # Change value in cell B2
        [(3, 2, "990909090021")]])  # Change value in cell B3
    def test_edit_and_upload_excel(self, modifications):
        filepath = "C:\\Users\\muhds\\Downloads\\Recruit_List_Template (4).xlsx"

        # Ensure the file is not in use and wait if necessary
        wait_time = 0
        while not os.access(filepath, os.W_OK) and wait_time < 10:
            time.sleep(1)
            wait_time += 1

        if not os.access(filepath, os.W_OK):
            pytest.fail(f"File {filepath} is not accessible after waiting.")

        workbook, sheet = load_excel_file(filepath)
        modify_excel_file(sheet, modifications)
        workbook.save(filepath)

    def test_login(self, consultant_maker_credentials):
        # Check if required credentials are provided
        if 'username' not in consultant_maker_credentials or 'password' not in consultant_maker_credentials:
            raise KeyError("The required keys 'username' or 'password' are missing in the credentials")

        # # Create a temporary file to store cookies
        # temp_file = tempfile.NamedTemporaryFile(delete=False)
        # temp_file.close()  # Close the file so it can be used by other processes
        #
        # # Initialize your cookies helper class
        # cookie_helper = CookiesHelper()
        #
        # # Delete existing cookies from the temporary file (if any)
        # cookie_helper.delete_cookies(temp_file.name)

        # Perform login actions
        login_page = LoginPage(self.driver)
        login_page.enter_username(consultant_maker_credentials["username"])
        login_page.enter_password(consultant_maker_credentials["password"])
        login_page.clickSubmit()
        self.wait()

        # Perform additional actions after login
        login_page.select_role('D-C-MKR', 'value')
        login_page.clickSubmit()
        self.wait()



        # # Store cookies after the submission
        # cookie_helper.store_cookies(self.driver, temp_file.name)
        # print(f"Cookies stored in: {temp_file.name}")
        #
        # # Clean up the temporary file
        # os.remove(temp_file.name)  # Delete the temporary file after use


    # def test_navToRecruitList(self):
    #     print("hello world")
    #     mainpage = MainPage(self.driver)
    #
    #     self.retry_find_element(mainpage.ConsultantMenu)
    #     # self.WaitElementPresent(mainpage.ConsultantMenu)
    #     mainpage.ClickConsultantMenu()
    #     self.WaitElementPresent(mainpage.RecruitListSubmenu)
    #     mainpage.ClickRecruitListSubmenu()

    def test_nav_to_recruit_list(self):
        main_page = MainPage(self.driver)

        self.retry_find_element(main_page.ConsultantMenu)

        retry_count = 3
        for attempt in range(retry_count):
            try:
                main_page.ClickConsultantMenu()
                main_page.ClickRecruitListSubmenu()
                break  # If successful, break out of the loop
            except StaleElementReferenceException:
                if attempt < retry_count - 1:
                    print("StaleElementReferenceException encountered. Retrying...")
                else:
                    raise  # Re-raise the exception if the last attempt fails

    def test_upload_recruit_list(self):
        recruitpage = RecruitPage(self.driver)

        self.retry_find_element(RecruitPage.RecruitText)
        retry_count = 3
        for attempt in range(retry_count):
            try:
                recruitpage.ClickUploadFilesButton()
                recruitpage.SelectScheme('UTS','value')
                break  # If successful, break out of the loop
            except StaleElementReferenceException:
                if attempt < retry_count - 1:
                    print("StaleElementReferenceException encountered. Retrying...")
                else:
                    raise  # Re-raise the exception if the last attempt fails












