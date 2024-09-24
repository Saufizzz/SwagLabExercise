import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div") # from parent to child
print(len(results))
assert len(results) > 0
actual_list = []
for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text) #chain method
    result.find_element(By.XPATH,"div/button").click() #should be //div[@class='products']/div/div/button
    print(actual_list)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

amount = (driver.find_elements(By.XPATH,"//tr/td[5]/p"))
sum = 0
for amt in amount:
    sum = sum + int(amt.text)

print(sum)
total_amount = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
assert sum == (total_amount)


driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)

#discount voucher
discount = driver.find_element(By.XPATH,"//span[@class='discountPerc']").text
disc = float(discount.strip('%'))/100
total_price = 0
if disc > 0:
    total_price = total_amount - (total_amount * disc)
print(total_price)

#total_discount = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)

assert total_amount >= total_price

# go to previous page and create list of title for fruit





