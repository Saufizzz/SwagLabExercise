from selenium.webdriver.common.by import By


class CheckOut:

    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    PostalCode = (By.XPATH, "//input[@id='postal-code']")
    ContinueBtn = (By.XPATH,"//input[@id='continue']")
    checkoutOverview = (By.XPATH, "//span[@class='title']")
    paymentinfo = (By.XPATH, "//div[normalize-space()='SauceCard #31337']")
    shippinginfo = (By.XPATH, "//div[normalize-space()='Free Pony Express Delivery!']")
    price_total = (By.XPATH, "//div[@class='summary_subtotal_label']")
    price_element =(By.XPATH, "//div[@class='summary_subtotal_label']")



    def __init(self, driver):
        self.driver = driver

    def insert_firstName(self, name):
        self.driver.find_element(*checkOut.first_name).send_keys(name)

    def insert_LastName(self, last_name):
        self.driver.find_element(*checkOut.last_name).send_keys(last_name)

    def insert_PostalCode(self, code):
        self.driver.find_element(*checkOut.PostalCode).send_keys(code)

    def clickContinue(self):
        self.driver.find_element(*checkOut.ContinueBtn).click()

    def displayCheckoutOverview(self):
        return self.driver.find_element(checkOut.checkoutOverview)

    def get_price_element(self):
        return self.driver.find_element(*checkOut.price_element)
        # price_string = price_element.text  # Get the text, e.g., "Subtotal: $15.98"
        #
        # # Use regex to extract the numeric value
        # price_total = float(re.search(r"[\d.]+", price_string).group())