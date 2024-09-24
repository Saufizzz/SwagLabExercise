#headless is running driver without seeing any browser invocation
# if want to handle typical popup such as your connection is not private use ignore certificate
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_option = Options()
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
