from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()