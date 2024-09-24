
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)



#variable
item_list = []

#wait function
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//form/input[@type='search']").send_keys("ca")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
items = driver.find_elements(By.XPATH,"//div[@class='products']/div")
for item in items:
    item_list.append(item.find_element(By.XPATH,"h4").text)
    item.find_element(By.XPATH,"div/button").click()
print(item_list)

#click the link
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.implicitly_wait(5)
#wait for the page to load
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))

#validate item in the cart
items = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for item in items:
    sum = sum + int(item.text)
    print(sum)

#calculate final price

discount = driver.find_element(By.XPATH,"//span[@class='discountPerc']").text
disc = float(discount.strip("%"))/100

if disc > 0:
    final_price = sum - (sum * disc)
    print(final_price)

assert final_price == float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)







