from selenium.webdriver.common.by import By

class PostProfile:
    StartDate = (By.XPATH,"//input[@title='Start date']")
    EndDate = (By.XPATH,"//input[@title='End date']")
    Session = (By.XPATH,"//select[@id='session_code']")
    Venue = (By.XPATH,"//input[@title='Venue']")
    Hours = (By.XPATH,"//input[@title='Total Hours']")
    ModeOfDelivery = (By.XPATH,"//select[@id='mode_delivery']")
    AddSpeaker = (By.XPATH,"//i[@class='fa fa-user-plus']")
    SpeakerName = (By.XPATH,"//input[@id='s_name']")
    SpeakerProfile = (By.XPATH,"//input[@id='s_profile']")
    AddSpeakerBtn = (By.XPATH,"//button[@id='add-btn']")
    RemoveSpeakerBtn = (By.XPATH,"//i[@class='fa fa-trash']")
    SpeakerDatatable = (By.XPATH,"//div[@id='listSpeaker']")
    FetchSpeakerDetail = (By.XPATH,"//div[@id='listSpeaker']//tr/td[i]")
    SpeakerNameDataTable= (By.XPATH,"// td[normalize - space() = 'jenol']")
    ConfirmDelete = (By.XPATH,"//button[normalize-space()='confirm']")
    OKbtn = (By.XPATH,"//button[normalize-space()='ok']")
    NavUploadFileBtn = (By.XPATH,"//a[@id='pdetails']")
    NavAdditionalInfoBtn = (By.XPATH,"//a[@id='addinfo']")
    NextPage = (By.XPATH,"//i[@class='fa fa-arrow-right']")
    StartDateError = (By.XPATH,"//label[@id='date_start-error']")
    EndDateError = (By.XPATH,"//label[@id='date_end-error']")
    SessionError = (By.XPATH,"//label[@id='session_code-error']")
    VenueError = (By.XPATH,"//label[@id='venue-error']")
    DeliveryModeError = (By.XPATH,"//label[@id='mode_delivery-error']")
    SpeakerError = (By.XPATH,"//label[@id='speaker-error']")
    UploadFileRequiredError = (By.XPATH,"//label[@id='CVDT1-error']")
    AdditionalInfoRequiredError = (By.XPATH,"//label[@id='CVDT4-error']")
    NavUploadFeedback = (By.XPATH,"//a[@id='pfeedback']//i[@class='fa fa-upload']")
    DownloadParticipantTemplate = (By.XPATH,"//a[normalize-space()='Participant list template (CSV)']")
    NavUploadParticipantList = (By.XPATH,"//a[@id='participanlist']")
    DeclarationBox = (By.XPATH,"//input[@title='Declaration']")
    UploadFeedbackError = (By.XPATH,"//label[@id='CVDT3-error']")
    UploadParticipantListError = (By.XPATH,"//label[@id='CVDT2-error']")
    DeclarationError = (By.XPATH,"//label[@id='declaration-error']")
    SubmitBtn = (By.XPATH,"//button[normalize-space()='Submit']")
    saveasdraft = (By.XPATH,"//button[@id='save']")
    UploadFileFilepath = (By.XPATH,"//input[@id='filepath1']")
    AddInfoFilepath = (By.XPATH,"//input[@id='filepath1']")
    UploadBtn = (By.XPATH,"//button[normalize-space()='Upload']")
    UploadFeedbackFilepath = (By.XPATH,"//input[@id='filepath1']")
    UploadParticipantFilepath = (By.XPATH,"//input[@id='filepath1']")
    Declaration = (By.XPATH,"//input[@title='Declaration']")
    datatableUlpoadParticipant1 = (By.XPATH,"//table[@id='participantList1']// td[2]")
    datatableUlpoadParticipant3 = (By.XPATH,"//table[@id='participantList3']//td[2]")
    YesBtn = (By.XPATH,"//button[normalize-space()='Yes']")

    #to extract all names inside accepted datatable listing
    #// table[ @ id = 'participantList1'] // td[2]
    #//table[@id='participantList3']//td[2]

    #to click button remove
    #// div[ @ id = 'uploaded_participanlist'] // tr / td[3] / button

    #Use during removing speaker from datatable
    #NavToTrashBtn = (By.XPATH,"//div[@id='listSpeaker']//tr/td[2]/following-sibling::td[2]")


    def __init__(self,driver):
        self.driver = driver

    def InsertStartDate(self):
        return self.driver.find_element(*PostProfile.StartDate)

    def InsertEndDate(self):
        return self.driver.find_element(*PostProfile.EndDate)

    def SelectSession(self):
        return self.driver.find_element(*PostProfile.Session)

    def InsertVenue(self):
        return self.driver.find_element(*PostProfile.Venue)

    def InsertTotalHours(self):
        self.driver.find_element(*PostProfile.Hours).clear()
        return self.driver.find_element(*PostProfile.Hours)

    def SelectModeOfDelivery(self):
        return self.driver.find_element(*PostProfile.ModeOfDelivery)

    def ClickAddSpeaker(self):
        self.driver.find_element(*PostProfile.AddSpeaker).click()

    def AddSpeakerNameAndProfile(self, name, profile):
        self.driver.find_element(*PostProfile.SpeakerName).send_keys(name)
        self.driver.find_element(*PostProfile.SpeakerProfile).send_keys(profile)

    def ClickAddBtn(self):
        self.driver.find_element(*PostProfile.AddSpeakerBtn).click()

    def ClickUploadFile(self):
        self.driver.find_element(*PostProfile.NavUploadFileBtn).click()

    def ClickAdditionalFile(self):
        self.driver.find_element(*PostProfile.NavAdditionalInfoBtn).click()

    def NavtoNextPage(self):
        self.driver.find_element(*PostProfile.NextPage).click()

    def ClickUploadFeedback(self):
        self.driver.find_element(*PostProfile.NavUploadFeedback).click()

    def ClickUploadParticipant(self):
        self.driver.find_element(*PostProfile.NavUploadParticipantList).click()

    def SaveAsDraft(self):
        self.driver.find_element(*PostProfile.saveasdraft).click()

    def UploadFile(self):
        return self.driver.find_element(*PostProfile.UploadFileFilepath)

    def UploadFileAddInfo(self):
        return self.driver.find_element(*PostProfile.AddInfoFilepath)

    def UploadFeedback(self):
        return self.driver.find_element(*PostProfile.UploadFeedbackFilepath)

    def UploadParticipantList(self):
        return self.driver.find_element(*PostProfile.UploadParticipantFilepath)

    def ClickUpload(self):
        self.driver.find_element(*PostProfile.UploadBtn).click()

    def displaydatatable1(self):
        return self.driver.find_elements(*PostProfile.datatableUlpoadParticipant1)

    def displaydatatable3(self):
        return self.driver.find_elements(*PostProfile.datatableUlpoadParticipant3)

    def ClickSubmit(self):
        self.driver.find_element(*PostProfile.SubmitBtn).click()

    def ClickOK(self):
        self.driver.find_element(*PostProfile.OKbtn).click()

    def ClickDeclaration(self):
        self.driver.find_element(*PostProfile.Declaration).click()

    def ClickYesBtn(self):
        self.driver.find_element(*PostProfile.YesBtn).click()




