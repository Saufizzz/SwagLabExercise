from selenium.webdriver.common.by import By


class PreVet:
    datatable = (By.XPATH,"//table[@id='prevetting']")
    expected_program = "dsafa"
    program_names = (By.XPATH, "//tr/td[5]")

    def __init__(self,driver):
        self.driver= driver

    def find_datatable(self):
        return self.driver.find_elements(*PreVet.datatable)

    def find_data(self):
        self.driver.find_elements(*PreVet.program_names)
        for i, program in enumerate(*PreVet.program_names):
            if program.text == PreVet.expected_program:
                xpath_text = f"//tr[{i}]/td[8]//i[1]"
                button = self.driver.find_element(By.XPATH,xpath_text)
                button.click()
                break
