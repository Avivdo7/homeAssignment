from typing import Generator, Optional, cast
import allure
import pytest
from _pytest.reports import TestReport
from _pytest.runner import CallInfo
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from locators.locators import HordPageLocators
from utils.utils import wait_for_element


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """
     Initialize and configure a Chrome WebDriver instance for testing Hord's web application.
    :return: WebDriver instance
    """
    chrome_options = config_chrome_options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://staging-app.hord.fi/")
    driver.maximize_window()
    assert wait_for_element(driver, HordPageLocators.SIDEBAR, timeout=10), "Sidebar element did not load in time"
    yield driver
    driver.quit()


def config_chrome_options() -> Options:
    """
    create options for chromedriver instance
    :return: Options instance
    """
    chrome_options = Options()

    # Basic configuration
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    # Additional configurations
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--remote-debugging-port=9222")
    #chrome_options.add_argument("--headless")  # for headless environments
    #chrome_options.add_argument("--disable-gpu") #for headless environments
    #chrome_options.add_argument("--window-size=1920x1080")

    return chrome_options


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: CallInfo) -> Generator[None, None, TestReport]:
    """
    PyTest hook to handle the result of each test and take a screenshot if a test fails.
    :param item: Test item currently executed
    :param call: Info about test call, like details of an exception
    :return: TestReport instance with test outcome
    """
    # Execute test, get outcome
    outcome = yield
    report: TestReport = outcome.get_result()

    # Take screenshot if a test fails, attach it to an Allure report
    # Before this check if the test is a function
    if report.when == 'call' and report.failed and isinstance(item, pytest.Function):
        driver: Optional[WebDriver] = cast(Optional[WebDriver], item.funcargs.get("driver", None))
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name=f"{item.name}_screenshot", attachment_type=AttachmentType.PNG)