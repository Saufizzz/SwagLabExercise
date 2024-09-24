#This  section is to store all the important key for running the automated browser
# This is import section
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#This is automated browser open

import pytest
from selenium import webdriver
import time

@pytest.fixture
def browser():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Close the browser after the test
    driver.quit()


# Define multiple users as a list of tuples (username, password)
users = [
    ("Admin", "admin123"),
    #("sadmin", "WBTAWQ"),
    # Add more users as needed
]

@pytest.mark.parametrize("username, password", users)
def test_login(browser, username, password):
    # Open the website
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    browser.implicitly_wait(5)

    # Enter username and password
    browser.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    browser.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    browser.find_element(By.XPATH,"//a[normalize-space()='']").click()
    browser.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("test2")
    browser.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
    assert "test2" in browser.page_source, "Failed to find 'test2' in search results"

    # Assert the title of the website
    '''image_element = browser.find_element(By.XPATH, "//img[@src='https://fimm-dev.zanko.com.my/assets/img/fimm/fimm-logo.png']")
    assert image_element is not None, f"Image element not found with the specified src attribute for user: {username}"'''

time.sleep(5)
'''def test_open_website(browser):
    # Open the website
    browser.get("https://fimm-dev.zanko.com.my/")
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH,"//input[@id='username']").send_keys("990424116028")
    browser.find_element(By.XPATH,"//input[@id='Passwordss']").send_keys("@123QWea")
    browser.find_element(By.XPATH, "//button[@id='submit']").click()
    # Assert the title of the website
    image_element = browser.find_element(By.XPATH,"//img[@src='https://fimm-dev.zanko.com.my/assets/img/fimm/fimm-logo.png']")
    assert image_element is not None, "Image element not found with the specified src attribute"'''


'''chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()





driver.get("https://fimm-dev.zanko.com.my/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("990424116028")
driver.find_element(By.XPATH,"//input[@id='Passwordss']").send_keys("@123QWea")
driver.find_element(By.XPATH,"//button[@id='submit']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Consultant Management']").click()
driver.find_element((By.XPATH,"//a[normalize-space()='Registration']")).click()

#action = ActionChains(driver)
#action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
#action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()'''