from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#from selenium.webdriver.firefox.options import Options for firefox

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/client")
print(driver.title)
#if in developer code there is <a it is a link
#in html form is the parent class and div is the child class
#if want to locate from parent to child XPATH = "//form/div[1]/input", CSS = "form div:nth-child(2) input"
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("12345")
driver.find_element(By.ID, "confirmPassword").send_keys("12345")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click() #this is based on text
