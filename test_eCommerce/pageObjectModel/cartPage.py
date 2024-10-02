from selenium.webdriver.common.by import By

class CartPage:

    listOfItem = (By.XPATH, "//div[@class='cart_item']")
    removeBtn = (By.XPATH, "//div/button[@class='btn btn_secondary btn_small cart_button']")
    continueShoppingbtn = (By.XPATH, "//button[@id='continue-shopping']")
    checkOutBtn = (By.XPATH, "//button[@id='checkout']")
    cart_title = (By.XPATH, "//span[@class='title']")
    cartItemName = (By.XPATH, "//div[@class='inventory_item_name']")
    cartItemPrice = (By.XPATH, "//div[@class='inventory_item_price']")


    def __init__(self, driver):
        self.driver = driver

    def cartTitle(self):
        return self.driver.find_element(*CartPage.cart_title)

    def allAddedItem(self):
        return self.driver.find_elements(*CartPage.listOfItem)

    def RemoveBtn(self):
        return self.driver.find_elements(*CartPage.removeBtn)

    def clickContinueShoppingBtn(self):
        self.driver.find_element(*CartPage.continueShoppingbtn).click()

    def clickCheckOutBtn(self):
        self.driver.find_element(*CartPage.checkOutBtn).click()

    def cartItemNameDisplay(self):
        return self.driver.find_elements(*CartPage.cartItemName)

    def cartItemPriceDisplay(self):
        return self.driver.find_elements(*CartPage.cartItemPrice)






