from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://malaysia.indeed.com/")
driver.find_element(By.ID,"text-input-what").send_keys("manual tester")
driver.find_element(By.CSS_SELECTOR,"button[class='yosegi-InlineWhatWhere-primaryButton']").click()
driver.find_element(By.XPATH,"//div/button[@id='filter-dateposted']").click()
dropdown = driver.find_elements(By.CSS_SELECTOR,"li[class='yosegi-FilterPill-dropdownListItem'] a")
for i in dropdown:
    if i.text == "Last 3 days":
        i.click()
        break

print(len(dropdown))
