from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


# variable
BrowserSortedVeggie = []

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
# assert the logo is present
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(5)
assert driver.find_element(By.XPATH,"//div[@class='brand greenLogo']").is_displayed()

#click top deal button and jump to a new page
driver.find_element(By.XPATH,"//a[@class='cart-header-navlink'][1]").click()
main_window = driver.window_handles
driver.switch_to.window(main_window[1])

#click on column header
#click on veggie names -> browserSortveggieList (B, A, C)
#sort this veggie list to get new SortedList this (A ,B ,C)
# browserSortveggielist == newSortedList
# this will failed if the browserSortVeggieList != newSortedList on assertion
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#if dont have cssselectorshub, can go to console type $x("//tr/td[1]") $x for XPATH $ for CSS
BrowserSortedVeggieList = driver.find_elements(By.XPATH,"//tr/td[1]")

# append list value inside variable browser sortedveggie using append
for Veggie in BrowserSortedVeggieList:
    BrowserSortedVeggie.append(Veggie.text)
# to avoid original value from changing, assign new variable to the original variable using copy/slice method
New_list = BrowserSortedVeggie.copy()
New_list.sort()
print(BrowserSortedVeggie)
print(New_list)
assert New_list == BrowserSortedVeggie