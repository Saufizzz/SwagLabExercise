import os
import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

base_url = "https://fimm-dev.zanko.com.my/"

# Load configuration from JSON file
@pytest.fixture
def consultant_maker_credentials(request):
    role = request.config.getoption("role")
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    credentials = config.get(role, {})

    if not credentials:
        raise KeyError(f"No credentials found for role: {role}")

    if 'username' not in credentials or 'password' not in credentials:
        raise KeyError("The required keys 'username' or 'password' are missing in the credentials")

    print(f"Loaded credentials for role '{role}': {credentials}")  # Debug print

    return credentials

# Add browser name/role as a command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )
    parser.addoption(
        "--role", action="store", default="consultant_maker1",  # Default role if none is specified
    )

# Fixture for setup and teardown of the WebDriver
@pytest.fixture(scope="class")
def setup_and_teardown(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.geckodriver()
    elif browser_name == "IE":
        driver = webdriver.IE()
    elif browser_name == "Safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Browser not supported!")


    driver.get(base_url)
    driver.maximize_window()
    #The WebDriver instance is assigned to request.cls.driver, which makes it accessible to test classes that are marked with @pytest.mark.usefixtures("setup_and_teardown").
    request.cls.driver = driver
    yield
    driver.quit()

# Hook to capture screenshots on test failures
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshots in the HTML report whenever a test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    # Fetch the WebDriver instance from the test class
    driver = getattr(item.instance, 'driver', None)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            if driver:
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name, driver)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extras.append(pytest_html.extras.html(html))
        report.extras = extras

# Function to capture a screenshot
def _capture_screenshot(name, driver):
    driver.get_screenshot_as_file(name)
