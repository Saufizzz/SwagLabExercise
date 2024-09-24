from selenium.webdriver.common.by import By


class PreProf:
    start_date = (By.XPATH,"//input[@title='Start date']")
    end_date = (By.XPATH,"//input[@title='End date']")
    session_code = (By.XPATH,"//select[@id='session_code'")
    Venue = (By.XPATH, "//input[@title='Venue']")
    Total_hours = (By.XPATH, "//input[@title='Total Hours']")
    mode_delivery = (By.XPATH, "//select[@id='mode_delivery']")
    addSpeaker = (By.XPATH, "//i[@class='fa fa-user-plus']")
    ID_Name = (By.XPATH, "//input[@id='s_name']")
    ID_Profile = (By.XPATH, "//input[@id='s_profile']")
    add_button = (By.XPATH, "//button[@id='add-btn']")
    file1 = (By.XPATH, "//a[@id='pdetails']//i[@class='fa fa-upload']")
    upload_file = (By.XPATH, "//input[@id='filepath1']")
    clickbtn = (By.XPATH, "//button[normalize-space()='Upload']")
    OKbtn = (By.XPATH, "//div[@role='dialog']//button[@class='btn btn-default']")



    def __init__(self,driver):
        self.driver = driver

    def InsStartDate(self):
        self.driver.find_element(*PreProf.start_date).send_keys("05072024")

    def InsEndDate(self):
        self.driver.find_element(*PreProf.end_date).send_keys("05102024")

    def SelSessCode(self):
        return self.driver.find_element(*PreProf.session_code)

    def InsVenue(self):
        self.driver.find_element(*PreProf.Venue).send_keys("Wilayah Persekutuan Kuala Lumpur")

    def InsTotalHours(self):
        self.driver.find_element(*PreProf.Total_hours).send_keys("8")

