import pickle
import os
#
# No Direct Driver Initialization: CookiesHelper does not initialize or manage the driver. It only uses it. This keeps it focused solely on cookie management.
#
# Flexibility: By passing driver as a parameter, CookiesHelper can be used with different WebDriver instances or configurations as needed.
#
# Integration: The driver is typically obtained from the test setup (like in conftest.py) and then passed to CookiesHelper methods when needed.
class CookiesHelper:
    def store_cookies(self, driver, file_path):
        cookies = driver.get_cookies()
        with open(file_path, 'wb') as f:
            pickle.dump(cookies, f)

    def load_cookies(self, driver, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                cookies = pickle.load(f)
                for cookie in cookies:
                    driver.add_cookie(cookie)

    def delete_cookies(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
