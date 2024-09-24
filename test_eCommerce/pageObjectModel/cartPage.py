from selenium.webdriver.common.by import By

class CartPage:
    listofItem = (By.XPATH, "//div[@class='cart_item']")
    removeBtn = (By.XPATH, "//div/button[@class='btn btn_secondary btn_small cart_button']")
    continueShoppingbtn = (By.XPATH, "//button[@id='continue-shopping']")
    checkOutBtn = (By.XPATH, "//button[@id='checkout']")
    cart_title = (By.XPATH, "//span[@class='title']")

    def __init__(self, driver):
        self.driver = driver

    def cartTitle(self):
        return self.driver.find_element(*CartPage.cart_title)


    def allAddedItem(self):
        return self.driver.find_elements(*CartPage.listofItem)

    def RemoveBtn(self):
        return self.driver.find_elements(*CartPage.removeBtn)

    def clickContinueShoppingBtn(self):
        self.driver.find_element(*CartPage.continueShoppingbtn).click()

    def clickCheckOutBtn(self):
        self.driver.find_element(*CartPage.checkOutBtn).click()

