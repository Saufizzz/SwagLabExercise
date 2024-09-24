#how to handle java popups using selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"input[id='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"input[id='alertbtn']").click()
#for clicking popup from java need to change from browser to alert mode
alert = driver.switch_to.alert
AlertText = alert.text
print(AlertText)
assert "Rahul" in AlertText
alert.accept() #method to replace OK clicking
#alert.dismissed() # method to replace cancel clicking
