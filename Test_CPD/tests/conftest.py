import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.geckodriver()
    elif browser_name == "IE":
        driver = webdriver.IE()
    elif browser_name == "Safari":
        driver = webdriver.Safari()

        # Handle Basic Authentication or Login Page
    auth_url = "https://fimm-dev.zanko.com.my/"
    username = "fimm-user"
    password = "ZankoFimm2024"

    # Uncomment and use the following line if basic authentication is used
    auth_url = f"https://{username}:{password}@fimm-dev.zanko.com.my/"


    driver.get(auth_url)
    driver.maximize_window()
    body = driver.find_element(By.TAG_NAME,'body')
    for _ in range(3):  # Adjust the range if needed to get closer to 80%
        body.send_keys(Keys.CONTROL, Keys.SUBTRACT)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)  # Ensure driver is available here
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras

def _capture_screenshot(name):
    try:
        driver.get_screenshot_as_file(name)
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")


# @pytest.fixture(scope='session')
# def config():
#     return load_config()

@pytest.fixture(scope='function')
def consultant_maker_credentials(config):
    return config['roles']['consultant_maker']

