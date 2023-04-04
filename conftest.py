import pytest
from selenium import webdriver

DRIVERS = {
    'chrome': '/drivers/chromedriver',
    'firefox': '/drivers/geckodriver'
}


def pytest_addoption(parser):
    parser.addoption("--driver", default="chrome")


@pytest.fixture
def browser_instance(request):
    browser_name = request.config.getoption("--driver")
    if browser_name == 'chrome':
        browser = webdriver.Chrome(DRIVERS['chrome'])
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=DRIVERS['firefox'])
    browser.start_client()
    request.addfinalizer(browser.close)
    return browser


@pytest.fixture
def some_fixture():
    return 2
