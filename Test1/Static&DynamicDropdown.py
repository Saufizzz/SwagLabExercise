#static dropdown (whenever see select tag in developer html sources it means static
#dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1) #by default the index will be 0 which is in the website is male
#dropdown.select_by_visible_text("Female") #based on the text on the dropdown
#dropdown.select_by_value("teacher") #if the html got values can use selectby value
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") #a represent anchor in the developer html
print(len(countries))

for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break
# when using .text it should show pre-built page (when first open page)
#print(driver.find_element(By.ID,"autosuggest").text)
#use this method to print dynamic dropdown value to use assert method
assert (driver.find_element(By.ID,"autosuggest").get_attribute("value")) == "India"