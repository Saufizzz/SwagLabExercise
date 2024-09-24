import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        #it will see if the checkbox has been click or not (boolean)
        assert checkbox.is_selected()
        break


radiobuttons = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton'")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
# if want to know whether an element is displayed on a page, is_displayed method will work
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()




