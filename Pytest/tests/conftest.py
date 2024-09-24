import pytest
from selenium import webdriver
driver = None # Global declaration of the driver variable

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    global driver # Declare that we are using the global driver variable
    browser_name = request.config.getoption("browser_name")
    # Instantiate the WebDriver based on the browser_name option
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.geckodriver()
    elif browser_name == "IE":
        driver = webdriver.IE()
    elif browser_name == "Safari":
        driver = webdriver.Safari()

    driver.get("https://fimm-dev.zanko.com.my/")
    driver.maximize_window()
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
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extras.append(pytest_html.extras.html(html))
            report.extras = extras

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

