import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2) #this step will wait 2 second function especially when writing find_elements and list.
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
assert len(results) > 0
for result in results:
    #this is chaining method from parent element to child element
    result.find_element(By.XPATH,"div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#can try use implicit if the send_keys button after progress to another page didnt work
#what implicit does is if the element on the page didnt show up, it will wait until 5 second before key in the strings
#difference with sleep is that sleep will sleep based on the time given whereas implicit will wait until the browser load (if set 5 second and 2 second the browser already open saved 3 second)
driver.implicitly_wait(5) #global timeout
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()
wait = WebDriverWait(driver,10) #only targeting based on variable used.
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

#with implicit wait you are actually waiting wherever the element is not displayed
#if there is a bug or failure, implicit will still wait for certain duration of time before declaring it failed
#explicit can actually target 1 specific element and can set exclusively.
# better to have both implicit and explicit wait in code. explicit used to target particular element, implicit target global.

