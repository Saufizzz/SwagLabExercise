import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Type of browser: chrome, firefox, or IE"
    )
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against: dev, staging, prod"
    )


@pytest.fixture(scope="function")
def setup_and_teardown(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    env = request.config.getoption("env")

    urls = {
        "dev": "https://www.saucedemo.com/",
        "staging": "https://staging.example.com",
        "prod": "https://prod.example.com"
    }
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "Internet Explorer":
        driver = webdriver.Ie()

    url = urls.get(env, "https://www.saucedemo.com/")
    driver.get(url)
    driver.maximize_window()
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(3):  # Adjust the range if needed to get closer to 80%
        body.send_keys(Keys.CONTROL, Keys.SUBTRACT)
    request.cls.driver = driver
    yield
    driver.quit()


# combine allure with html for report generation screenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshots in both HTML and Allure reports
    whenever a test fails.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    # Only take action on the 'call' phase
    if report.when == 'call':
        # Check if the test failed
        if report.failed:
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)

            # 1. Attach screenshot to the Allure report
            allure.attach.file(file_name, name=file_name, attachment_type=allure.attachment_type.PNG)

            # 2. Embed screenshot in the HTML report
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


def _capture_screenshot(name):
    global driver #if unsuccessful check for this code
    try:
        driver.get_screenshot_as_file(name)
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")
