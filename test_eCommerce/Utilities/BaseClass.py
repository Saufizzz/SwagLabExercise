import inspect
import time
import pytest
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup_and_teardown")
class BaseClass:

    # Explicit Wait & Implicit Wait
    def WaitElementClickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def WaitElementPresent(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def Wait(self, seconds):
        return self.driver.implicitly_wait(seconds)

    # ActionChains Method

    def ActionMove(self, locator):
        """
        Moves to the specified element and performs a click action.

        :param locator: The element you want to move to and click.
        """
        ActionChains(self.driver).move_to_element(locator).click().perform()

    # Select Method


    def SelectByType(self, locator, select_type, value):
        """
        Selects an option from a dropdown based on the specified selection type.

        :param locator: The dropdown WebElement.
        :param select_type: The type of selection ('index', 'text', 'value').
        :param value: The value or index to be selected (integer for 'index', string for 'text' and 'value').
        """
        select = Select(locator)

        if select_type == "index":
            # Ensure value is converted to an integer when selecting by index
            return select.select_by_index(int(value))
        elif select_type == "text":
            return select.select_by_visible_text(value)
        elif select_type == "value":
            return select.select_by_value(value)
        else:
            raise ValueError(f"Invalid selection type: {select_type}. Use 'index', 'text', or 'value'.")

    # Scroll Product

    def scrollAndLoadAllProduct(self):
        Scroll_pause_time = 1  # Adjust this pause time as necessary
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(Scroll_pause_time)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    # Retry Action

    def retry_action(action, max_attempts=3, delay=1):
        attempts = 0
        while attempts < max_attempts:
            try:
                # Attempt the action
                result = action()
                return result  # Return the result if successful
            except Exception as e:
                # Handle the exception (or you can just pass)
                print(f"Attempt {attempts + 1} failed:", e)
                # Increment attempts counter
                attempts += 1
                # Wait for a short delay before retrying
                time.sleep(delay)
        # If max_attempts reached without success, raise an exception
        raise Exception("Max attempts reached without success")

    def getLogger(self):
        # This line retrieves the name of the calling function.
        loggerName = inspect.stack()[1][3]

        # This line creates or retrieves a logger object using the name of the calling function.
        logger = logging.getLogger(loggerName)

        # Check if the logger has handlers already to avoid duplicate logs.
        if not logger.handlers:
            # Create a FileHandler object to write log records to a file.
            filehandler = logging.FileHandler("logfile.log")

            # Create a Formatter object with the specified format.
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

            # Set the formatter to the FileHandler.
            filehandler.setFormatter(formatter)

            # Add the FileHandler to the logger.
            logger.addHandler(filehandler)

            # Optionally, set the logging level. For example, to DEBUG.
            logger.setLevel(logging.DEBUG)

        return logger










