from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#different locator selenium provide ( ID, Xpath, CSSSelector, Classname, name, linkText)
# to check for locator, right click and inspect the boxes to show developer tools.
#import new package
# for any element xpath and cssselector can be used not like name id linktext which is dependent on developer
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

#static dropdown (whenever see select tag in developer html sources it means static
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1) #by default the index will be 0 which is in the website is male
dropdown.select_by_visible_text("Female") #based on the text on the dropdown
#dropdown.select_by_value("teacher") #if the html got values can use selectby value



#For Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
#Create CSSselector - tagname[attribute='value'] -> input[type='submit']
#can be validate in inspect browser on selectorshubs tab can type input or #id. / .classname
#if there are multiple same element in the page can used (//input[@type='text'])[3] based on the xpath value.
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

print(message)
assert "Success" in message #if there is no word in the variable the assert will fail the test

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hallo Again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

