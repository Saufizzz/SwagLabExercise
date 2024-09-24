from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//a[@target='_blank']").click()

#change windows from parent to child
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
username = (driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text)
driver.close()


driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH,"//input[@type='text']").send_keys(username)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("12345")
dropdown = Select(driver.find_element(By.XPATH,"//select"))
dropdown.select_by_value("teach")
driver.find_element(By.XPATH,"//input[@id='terms']").click()
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@style='display: block;']")))
alert = driver.find_element(By.XPATH,"//div[@style='display: block;']").text
print(alert)

assert alert == "Incorrect username/password."

driver.refresh()






