#1. another method but still need to troubleshoot the issue
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

# chrome cannot be invoked directly need to installed chrome driver
#service_object = Service(r"C:\Users\muhds\PycharmProjects\chromedriver_win32/geckodriver.exe")
#driver = webdriver.Firefox(service=service_object)
# responsible to get url in browser
#driver.get("https://rahulshettyacademy.com")
#driver.close()




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options for firefox


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com')
print(driver.title)
print(driver.current_url)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()




