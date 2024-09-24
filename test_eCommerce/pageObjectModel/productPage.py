from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass



class ProductPage:
    productName = (By.XPATH, "//div[@class='inventory_item']//a/div")
    price = (By.XPATH, "//div[@class='inventory_item_price']")
    addToCartBtn = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
    listItem = (By.XPATH,"//div[@class='inventory_list']/div")
    CartBtn = (By.XPATH, "//a[@class='shopping_cart_link']")
    selectSort = (By.XPATH, "//select[@class='product_sort_container']")

    def __init__(self, driver):
        self.driver = driver

    def listProductName(self):
        return self.driver.find_elements(*ProductPage.productName)

    def listProductPrice(self):
        return self.driver.find_elements(*ProductPage.price)

    def listOfAllItem(self):
        return self.driver.find_elements(*ProductPage.listItem)

    def addtoCartBtn(self):
        return self.driver.find_elements(*ProductPage.addToCartBtn)

    def navToCart(self):
        self.driver.find_element(*ProductPage.CartBtn).click()

    def selectoption(self):
        return self.driver.find_element(*ProductPage.selectSort)







