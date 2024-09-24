#driver only have access to local html. dont have access to embedded html
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/iframe")

#switch to frames (same step as switch to window)
driver.switch_to.frame("mce_0_ifr") #using frame.id or frame.name

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content() #whatever browser initially initiated it will revert back to original

assert driver.find_element(By.TAG_NAME,"h3").text == "An iFrame containing the TinyMCE WYSIWYG Editor"
