from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://rahulshettyacademy.com/angularpractice/")
assert driver.find_element(By.XPATH,"//div[@class='jumbotron']").is_displayed()

#click on the shop
#can use //a[contains(@href,'shop')] (regular expression/regex) will detect partial value XPATH
# a[href*='Shop'] regex for CSS
driver.find_element(By.LINK_TEXT,"Shop").click()
phones = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
#using chain web element
for phone in phones:
    phone_name = phone.find_element(By.XPATH,"div/h4/a").text
    if phone_name == "Blackberry":
        phone.find_element(By.XPATH,"div/button").click()

#driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()

driver.find_element(By.XPATH,"//td/button[@class='btn btn-success']").click()

driver.find_element(By.XPATH,"//input[@id='country']").send_keys("Ma")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Germany")))
driver.find_element(By.LINK_TEXT,"Germany").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successText = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

assert "Success!" in successText



