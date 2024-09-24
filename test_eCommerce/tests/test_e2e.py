import allure

from Utilities.BaseClass import BaseClass
from pageObjectModel.cartPage import CartPage
from pageObjectModel.loginPage import LoginPage
from pageObjectModel.productPage import ProductPage
from allure_commons.types import AttachmentType


class TestE2E(BaseClass):
    username = "standard_user"
    password = "secret_sauce"

    def test_invalid_credentials(self):
        login = LoginPage(self.driver)
        login.insertUsername("sasd")
        login.insertPassword(self.password)
        login.clickLoginBtn()
        assert login.errMsg().is_displayed, "error Not Found"

    @allure.step("Sort the order of the item")
    def test_sort(self):
        login=LoginPage(self.driver)
        login.insertUsername(self.username)
        login.insertPassword(self.password)
        login.clickLoginBtn()

        #sort the order
        product = ProductPage(self.driver)

        items = product.listOfAllItem()

        # Get all product names, prices, and add to cart buttons
        names = [name.text for name in product.listProductName()]
        prices = [price.text for price in product.listProductPrice()]

        # Combine the names, prices, and conditionally add items to cart
        all_items = [(names[i], prices[i]) for i in range(len(items))]

        # Print all items
        for name, price in all_items:
            print(f"Product: {name}, Price: {price}")
            
        self.SelectByType(product.selectoption(),"value", "za")

        all_items_sorted = [(names[i], prices[i]) for i in range(len(items))]
        for name, price in all_items_sorted:
            print(f"product: {name}, Price: {price}")

        assert all_items != all_items_sorted, "sorted error"





    @allure.step("Add to cart item end-to-end step")
    def test_add_to_cart(self):
        login = LoginPage(self.driver)
        login.insertUsername(self.username)
        login.insertPassword(self.password)
        login.clickLoginBtn()
        self.Wait(10)
        expected_title = "Swag Labs"
        actual_title = self.driver.title

        assert expected_title == actual_title, f"Title does not match! Expected: {expected_title}, but got: {actual_title}"

# Product Page
        product = ProductPage(self.driver)

        # Get a list of all items
        items = product.listOfAllItem()

        # Get all product names and prices
        names = product.listProductName()
        prices = product.listProductPrice()
        addCartBtn = product.addtoCartBtn()

        # Combine the names and prices and print them
        all_items = []
        added_item = []
        for i in range(len(items)):
            name = names[i].text
            price = prices[i].text
            print(f"Product: {name}, Price: {price}")

            if name in ["Sauce Labs Bolt T-Shirt", "Sauce Labs Bike Light"]:
                addCartBtn[i].click()
                added_item.append(name)
                print(f"Added {name} to the cart")

            # Optionally, you can append the name and price to the all_items list
            all_items.append((name, price))
            print(f"This is added item {added_item}")

        product.navToCart()

#CartPage
        cart = CartPage(self.driver)
        self.WaitElementPresent(cart.cart_title)
        assert cart.cartTitle().is_displayed(), "Display Wrong Page"












