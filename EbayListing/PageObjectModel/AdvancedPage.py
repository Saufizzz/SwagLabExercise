import time

from selenium.webdriver.common.by import By


class AdvancedPage:
    KeywordField = (By.XPATH, "//input[@id='_nkw']")
    AllCategoryDropDown = (By.XPATH, "//div[@class='field adv-field___sacat']//select[contains(@id,'s0-1-17-4')]")
    CompletedItems = (By.XPATH, "//fieldset[@class='adv-fieldset__searchIncluding']//div[2]//span[1]//input[1]")
    SoldItems = (By.XPATH, "//fieldset[@class='adv-fieldset__searchIncluding']//div[3]//span[1]//input[1]")
    LocatedIn = (By.XPATH, "//fieldset[@class='adv-fieldset__location']//div[6]//span[1]//input[1]")
    LocatedInDropdown = (By.XPATH, "//div[6]//span[2]//span[1]//select[1]")
    SortBy = (By.XPATH, "//fieldset[@class='adv-fieldset__miscSelects']//div[1]//div[1]//span[1]//select[1]")
    Search = (By.XPATH, "//div[@class='adv-form__actions']//button[@type='submit'][normalize-space()='Search']")

    def __init__(self, driver):
        self.driver = driver

    def InputKeywordField(self, text):
        self.driver.find_element(*AdvancedPage.KeywordField).send_keys(text)

    def SelCategory(self):
        return self.driver.find_element(*AdvancedPage.AllCategoryDropDown)

    def clickCompleteddItem(self):
        self.driver.find_element(*AdvancedPage.CompletedItems).click()

    def clickSoldItem(self):
        self.driver.find_element(*AdvancedPage.SoldItems).click()

    def clickLocatedIn(self):
        self.driver.find_element(*AdvancedPage.LocatedIn).click()

    def SelLocatedIn(self):
        return self.driver.find_element(*AdvancedPage.LocatedInDropdown)

    def SelSortBy(self):
        return self.driver.find_element(*AdvancedPage.SortBy)

    def clickSearch(self):
        self.driver.find_element(*AdvancedPage.Search).click()

    def search_item(self, item_name, item_locator, next_button_locator):
        while True:
            try:
                # Check if the item is present on the current page
                items = self.driver.find_elements(item_locator)
                for item in items:
                    if item_name.lower() in item.text.lower():
                        print(f"Item '{item_name}' found.")
                        return True

                # Move to the next page
                next_button = self.driver.find_element(next_button_locator)
                if next_button.is_enabled():
                    next_button.click()
                    time.sleep(3)  # Wait for the page to load
                else:
                    print(f"Item '{item_name}' not found in any page.")
                    return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False

    def print_all_items_in_column(self, column_locator, next_button_locator):
        all_items = []  # List to store all items across pages
        while True:
            try:
                # Extract items from the specified column on the current page
                items = self.driver.find_elements(column_locator)
                item_texts = [item.text for item in items if item.text.strip()]
                all_items.extend(item_texts)

                # Print all collected items from the column
                print(f"Items in column across pages: {', '.join(all_items)}")

                # Move to the next page
                next_button = self.driver.find_element(next_button_locator)
                if next_button.is_enabled():
                    next_button.click()
                    time.sleep(3)  # Wait for the page to load
                else:
                    print("No more pages to navigate.")
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
                break
