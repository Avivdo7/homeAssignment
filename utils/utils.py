import logging
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def scroll_into_view(driver: WebDriver, element: WebElement) -> None:
    """
    Scrolls the target element into view by executing JavaScript.
    :param driver: WebDriver instance
    :param element: WebElement to scroll into view
    :return: None
    """
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    WebDriverWait(driver, 10).until(EC.visibility_of(element))  # Use WebDriverWait instead of time.sleep


def click_element(driver: WebDriver, element: WebElement) -> None:
    """
    Performs a click action on the specified element using JavaScript.
    :param driver: WebDriver instance
    :param element: The element to be clicked
    :return: None
    """
    driver.execute_script("arguments[0].click();", element)


def is_element_present(driver: WebDriver, locator: Tuple[By, str]) -> bool:
    """
    Checks if the element located by the specified locator is present on the page.
    :param driver: WebDriver instance
    :param locator: Locator tuple specifying the method and target element
    :return: True if the element is found, False otherwise
    """
    try:
        driver.find_element(*locator)
        return True
    except NoSuchElementException:
        return False


def hover_element(driver: WebDriver, locator: Tuple[By, str]) -> None:
    """
    Moves the mouse pointer over the specified element on the page.
    :param driver: WebDriver instance
    :param locator: Locator tuple specifying the element to hover over
    :return: None
    """
    element: WebElement = driver.find_element(*locator)
    action = ActionChains(driver)
    action.move_to_element(element).perform()


def wait_for_element(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> bool:
    """
    Waits until the specified element is visible on the page within a given time limit.
    :param driver: WebDriver instance
    :param locator: Locator tuple specifying the element to wait for
    :param timeout: Maximum time to wait for the element, default is 10 seconds
    :return: True if the element becomes visible, False otherwise
    """
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        logger.error(f"Element {locator} not found on page within {timeout} seconds.")
        return False


def wait_until_clickable(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> bool:
    """
    Waits until the specified element is clickable within a given time limit.
    :param driver: WebDriver instance
    :param locator: Locator tuple specifying the element to wait for
    :param timeout: Maximum time to wait for the element to become clickable, default is 10 seconds
    :return: True if the element becomes clickable, False otherwise
    """
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        return True
    except TimeoutException:
        logger.error(f"Element {locator} was not clickable within {timeout} seconds.")
        return False
