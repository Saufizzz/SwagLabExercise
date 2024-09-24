from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

#ensure logo is displayed
assert driver.find_element(By.XPATH,"//img[@class='logoClass']").is_displayed()

# identify all checkboxes and tick the 2nd
radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio in radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()

assert driver.find_element(By.XPATH,"//input[@value='radio2']").is_selected()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()

assert checkbox.find_element(By.XPATH,"//input[@value='option2']").is_selected()


#using action chain for dynamic dropdown
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("br")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//div[text()='Brazil']")).click().perform()

#using select method for static dropdown
dropdown = Select(driver.find_element(By.XPATH,"//select"))
dropdown.select_by_index(1)

#using window handles to handle new tab or new window popup
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
new_window = driver.window_handles
driver.current_window_handle
driver.switch_to.window(new_window[1])
assert driver.find_element(By.XPATH,"//div[@id='banner']").is_displayed()
driver.close()
driver.switch_to.window(new_window[0])

#how to perform javascript action using python
#go to console and type window.scrollBy(x,y);axis
#if want to go to the bottom of the page window.scrollBy(0,document.body.scrollHeight)
driver.execute_script("window.scrollBy(0,1400);")

#how to take screenshot in python (basic without framework)
#driver.get_screenshot_as_file("screen.png")

driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Practice").click()
#action.move_to_element(driver.find_element(By.XPATH,"//li[@class='dropdown open']")).perform()
#driver.switch_to.default_content()


#frame convert
#can use id or name
#driver.switch_to.frame("frame name/frame id")
#driver.switch_to.default_content()



#driver.find_element(By.XPATH,"//a[@id='opentab']").click()
#driver.switch_to.window(new_window[1])
#assert driver.find_element(By.XPATH,"//img[@alt='First slide']").is_displayed()
#driver.close()








