import os.path
import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
from PageObjects.PostVetPage import PostVetPage
from PageObjects.PostVetProfile import PostProfile
from Utilities.BaseClass import BaseClass

class Test_e2e_PostVetting(BaseClass):

    # def test_login_distributor(self):
    #     loginPage = LoginPage(self.driver)
    #     loginPage.InsName("muzahar@adf.com.my")
    #     loginPage.InsPassword("@1234qweR")
    #     loginPage.clickSubmit()
    #     self.wait()
    #     self.SelectIndex(loginPage.SelectRole(), 2)
    #     loginPage.clickSubmit()
    #     time.sleep(5)

    def test_MainPage(self):
        mainPage = MainPage(self.driver)
        mainPage.NavCPDMenu()
        mainPage.NavPostVet()


    @pytest.mark.parametrize("title, StartDate,EndDate, Venue, Hours, SpeakersName, SpeakersProfile",[
         ("kaki step", "02102024", "02102024", "Wisma KL", "10", "Zulhasnain", "Cikgu Sekolah Menengah"
          )
    ])
    def test_add_PostVet_program(self,title, StartDate, EndDate, Venue, Hours, SpeakersName,SpeakersProfile):
        postvetpage = PostVetPage(self.driver)
        postvetprofile = PostProfile(self.driver)

        upload_file_path = os.path.join(r"C:\\Users\\muhds\\Desktop\\FIMM-Consent-Form (1).pdf")
        upload_participant_file = os.path.join(r"C:\\Users\\muhds\\Downloads\\Upload_Participant_Template.csv")


        postvetpage.ClickAddProgram()
        self.ScrollAndLoadAllProducts()
        postvetpage.InsertProgTitle().send_keys(title)
        postvetpage.ClickProceedBtn()
        self.wait()
        self.ScrollAndLoadAllProducts()
        postvetprofile.InsertStartDate().send_keys(StartDate)
        postvetprofile.InsertEndDate().send_keys(EndDate)
        self.ScrollAndLoadAllProducts()
        self.SelectByText(postvetprofile.SelectSession(),"FULL DAY")
        postvetprofile.InsertVenue().send_keys(Venue)
        postvetprofile.InsertTotalHours().send_keys(Hours)
        self.SelectByValue(postvetprofile.SelectModeOfDelivery(),"CVM2")
        postvetprofile.ClickAddSpeaker()
        postvetprofile.AddSpeakerNameAndProfile(SpeakersName, SpeakersProfile)
        postvetprofile.ClickAddBtn()
        self.ScrollAndLoadAllProducts()
        self.wait()
        postvetprofile.ClickUploadFile()
        self.wait()
        postvetprofile.UploadFile().send_keys(upload_file_path)
        self.WaitElementClickable(postvetprofile.UploadBtn)
        postvetprofile.ClickUpload()
        self.WaitElementClickable(PostProfile.OKbtn)
        postvetprofile.ClickOK()
        self.wait()
        self.ScrollAndLoadAllProducts()
        postvetprofile.ClickAdditionalFile()
        self.wait()
        postvetprofile.UploadFileAddInfo().send_keys(upload_file_path)
        self.WaitElementClickable(postvetprofile.UploadBtn)
        postvetprofile.ClickUpload()
        self.WaitElementClickable(PostProfile.OKbtn)
        postvetprofile.ClickOK()
        self.wait()
        self.ScrollAndLoadAllProducts()
        self.WaitElementPresent(PostProfile.NextPage)
        postvetprofile.NavtoNextPage()
        self.wait()
        postvetprofile.ClickUploadFeedback()
        self.wait()
        postvetprofile.UploadFeedback().send_keys(upload_file_path)
        self.WaitElementClickable(postvetprofile.UploadBtn)
        postvetprofile.ClickUpload()
        self.WaitElementClickable(PostProfile.OKbtn)
        postvetprofile.ClickOK()
        self.wait()
        self.ScrollAndLoadAllProducts()
        postvetprofile.ClickUploadParticipant()
        self.wait()
        postvetprofile.UploadParticipantList().send_keys(upload_participant_file)
        self.WaitElementClickable(postvetprofile.UploadBtn)
        postvetprofile.ClickUpload()
        self.WaitElementClickable(PostProfile.OKbtn)
        postvetprofile.ClickOK()
        self.ScrollAndLoadAllProducts()
        data = []
        datatable1 = postvetprofile.displaydatatable1()
        datatable3 = postvetprofile.displaydatatable3()

        for i, applicantAccepted in enumerate(datatable1, start=1):
            print(applicantAccepted.text)
            data.append(applicantAccepted.text)


        for j, applicantNotExist in enumerate(datatable3, start=1):
            print(applicantNotExist.text)
            data.append(applicantNotExist.text)

        print(data)
        assert len(data) > 0, "No data extracted from the tables."

        postvetprofile.ClickDeclaration()
        postvetprofile.ClickSubmit()
        postvetprofile.ClickYesBtn()
        postvetprofile.ClickOK()


















