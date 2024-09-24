import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

driver = webdriver.Chrome()
driver.get("https://fimm-dev.zanko.com.my/")
driver.maximize_window()

file_path = os.path.abspath("C:\\Users\\user\\Desktop\\Doc1.pdf")

driver.find_element(By.XPATH, "//input[@id='username']").send_keys("iza.tp11@yopmail.com")
driver.find_element(By.XPATH, "//input[@id='Passwordss']").send_keys("@1234qweR")
driver.find_element(By.XPATH, "//button[@id='submit']").click()
driver.implicitly_wait(10)
role = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='role']")))
select_role = Select(role)
select_role.select_by_index(0)
driver.find_element(By.XPATH, "//button[@id='submit']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Continuing Professional Development']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Pre-Vetting']").click()
driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//a[normalize-space()='Add New Program']").click()
# driver.find_element(By.XPATH,"//input[@id='title2']").send_keys("Joget Dangdut")
# driver.find_element(By.XPATH,"//button[@id='createApp']").click()
driver.execute_script("window.scrollBy(0,500)", "")
rows = driver.find_elements(By.XPATH, "//table[@id='prevetting']")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,300)", "")
# 1st method
"""i = 1
expected_program = "Joget Dangdut"
program_names = driver.find_elements(By.XPATH,"//tr/td[5]")
#xpath_text = "//td[normalize-space()='Joget Dangdut']"
for program in program_names:
    if program.text._eq_(expected_program):
        print(program.text)
        xpath_text = "//tr["+str(i)+"]/td[8]i[1]"
        button = driver.find_element(By.XPATH,xpath_text)
        button.click()
    i = i+1

time.sleep(10)
"""
expected_program = "dsafa"
# This line finds all elements that represent program names in the table.
# It uses XPath to locate <td> elements that are in the 5th column (td[5]) of each row (//tr).
program_names = driver.find_elements(By.XPATH, "//tr/td[5]")
# This loop iterates through each program name found in the table.
# enumerate() is used to get both the index i and the program name program. start=1 ensures that the index starts from 1 instead of 0.
for i, program in enumerate(program_names, start=1):
    print(program.text)
    if program.text == expected_program:
        xpath_text = f"//tr[{i}]/td[8]//i[1]"
        button = driver.find_element(By.XPATH, xpath_text)
        button.click()
        break  # Exit loop after clicking the button

# @pytest.mark.parametrize("start_date,end_date,Venue,Total_hours,name,profile",[
#     ("05072024", "05102024","Wilayah Persekutuan Kuala Lumpur", "8", "Zakwan", "Cikgu Sekolah")
# ]
#                          )
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@title='Start date']").send_keys("05072024")
driver.find_element(By.XPATH, "//input[@title='End date']").send_keys("05102024")
selectSession = Select(driver.find_element(By.XPATH, "//select[@id='session_code']"))
selectSession.select_by_index(0)
driver.find_element(By.XPATH, "//input[@title='Venue']").send_keys("Wilayah Persekutuan Kuala Lumpur")
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, "//input[@title='Total Hours']").send_keys("8")
ModeOfDelivery = Select(driver.find_element(By.XPATH, "//select[@id='mode_delivery']"))
ModeOfDelivery.select_by_index(1)
driver.find_element(By.XPATH, "//i[@class='fa fa-user-plus']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@id='s_name']").send_keys("Zakwan")
driver.find_element(By.XPATH, "//input[@id='s_profile']").send_keys("Cikgu Sekolah")
driver.find_element(By.XPATH, "//button[@id='add-btn']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@id='pdetails']//i[@class='fa fa-upload']").click()
driver.find_element(By.XPATH, "//input[@id='filepath1']").send_keys(file_path)
driver.find_element(By.XPATH, "//button[normalize-space()='Upload']").click()
driver.find_element(By.XPATH, "//div[@role='dialog']//button[@class='btn btn-default']").click()
# success_text = driver.find_element(By.XPATH,"//*[@id='jconfirm-box43858']").text()
# assert success_text.is_displayed(), "ErrorOccured"
time.sleep(5)

driver.find_element(By.XPATH, "//a[@id='addinfo']//i[@class='fa fa-upload']").click()
driver.find_element(By.XPATH, "//input[@id='filepath1']").send_keys(file_path)
time.sleep(5)
driver.find_element(By.XPATH, "//button[normalize-space()='Upload']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()