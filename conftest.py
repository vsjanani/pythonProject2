import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
webdriverObj = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge", help="my option: chrome or edge"
    )


@pytest.fixture(scope="class")
def test_dawn_dusk(request):
    global webdriverObj
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        serviceObj = Service("C:/Users/dines/OneDrive/Documents/MyPythonProject/chromedriver.exe")
        webdriverObj = webdriver.Chrome(service=serviceObj)
    elif browser_name == "edge":
        serviceObj = Service("C:/Users/dines/OneDrive/Documents/MyPythonProject/msedgedriver.exe")
        webdriverObj = webdriver.Edge(service=serviceObj)
    elif browser_name == "firefox":
        print("Hi, I am firefox")
    else:
        print("Invalid browser_name, type it right honey !!")
    # webdriverObj.get("http://automationpractice.com/index.php")
    webdriverObj.get("https://www.amazon.in")
    webdriverObj.maximize_window()
    webdriverObj.implicitly_wait(10)
    mouseHover = ActionChains(webdriverObj)
    request.cls.webdriverObj = webdriverObj
    request.cls.mouseHover = mouseHover
    yield
    webdriverObj.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        webdriverObj.get_screenshot_as_file(name)
