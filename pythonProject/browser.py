import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

time.sleep(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)]").click()

# Locate the sidebar element
sidebar_element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]")

# Create an ActionChains object
actions = ActionChains(driver)

# Perform a series of actions
actions.click(sidebar_element).perform()
driver.implicitly_wait(5)

# Optionally, you can chain more actions, for example, clicking on a specific item within the sidebar
# submenu_element = driver.find_element(By.XPATH, "//your/sidebar/submenu/xpath")
# actions.click(submenu_element).perform()

# Close the browser
driver.quit()
