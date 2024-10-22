import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.hord_page import HordPage
from utils.utils import scroll_into_view


@allure.feature('Sidebar functionality')
class TestSidebar:

    @allure.story('Sidebar should be open by default after page load')
    @pytest.mark.usefixtures("driver")
    def test_sidebar_open_after_page_load(self, driver: WebDriver) -> None:
        """
        Ensure that the sidebar is open by default after loading the Hord page.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        with allure.step("Verify sidebar is not collapsed on page load"):
            assert not hord_page.is_sidebar_collapsed, "Sidebar should be open by default"

    @allure.story('Sidebar can be collapsed using the toggle button')
    @pytest.mark.usefixtures("driver")
    def test_sidebar_can_be_collapsed(self, driver: WebDriver) -> None:
        """
        Test that the sidebar can be collapsed using the toggle button.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        hord_page.click_toggle_button_with_js()

        with allure.step("Verify sidebar collapses after toggle button click"):
            assert hord_page.is_sidebar_collapsed, "Sidebar should be collapsed after clicking toggle button"

    @allure.story('Sidebar can be reopened using the toggle button')
    @pytest.mark.usefixtures("driver")
    def test_sidebar_can_be_reopened(self, driver: WebDriver) -> None:
        """
        Test that the sidebar can be reopened using the toggle button after it was collapsed.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        hord_page.click_toggle_button_with_js()  # Collapse sidebar
        hord_page.click_toggle_button_with_js()  # Reopen sidebar

        with allure.step("Verify sidebar is reopened after second toggle"):
            assert not hord_page.is_sidebar_collapsed, "Sidebar should reopen after toggling again"


@allure.feature('FAQ section functionality')
class TestFAQSection:

    @allure.story('FAQ section should be visible on the page')
    @pytest.mark.usefixtures("driver")
    def test_faq_section_is_visible(self, driver: WebDriver) -> None:
        """
        Test that the FAQ section is visible on the Hord page.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        with allure.step("Verify that the FAQ section is present"):
            assert hord_page.is_faq_section_exists(), "FAQ section should be visible on the page"

    @allure.story('FAQ ETH staking question is visible')
    @pytest.mark.usefixtures("driver")
    def test_faq_eth_staking_question_visible(self, driver: WebDriver) -> None:
        """
        Test that the ETH staking question in the FAQ section is visible.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        with allure.step("Verify that the ETH staking question is present"):
            assert hord_page.is_faq_eth_exists(), "FAQ ETH staking question should be visible on the page"

    @allure.story('ETH staking question answer is visible')
    @pytest.mark.usefixtures("driver")
    def test_faq_eth_answer_visible(self, driver: WebDriver) -> None:
        """
        Test that the answer for the ETH staking question is visible after expanding the question.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        with allure.step("Verify that the answer for ETH staking question is present"):
            assert hord_page.is_faq_eth_answer_exists(), "Answer for ETH staking question should be visible"


@allure.feature('Last Airdrops section functionality')
class TestLastAirdrops:

    @allure.story('Last Airdrops section should be visible')
    @pytest.mark.usefixtures("driver")
    def test_last_airdrops_section_exists(self, driver: WebDriver) -> None:
        """
        Verify that the Last Airdrops section is present on the page.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        with allure.step("Check if Last Airdrops section is visible"):
            assert hord_page.is_last_airdrops_section_exists(), "Last Airdrops section should be visible on the page"

    @allure.story('Last Airdrops should contain epoch containers')
    @pytest.mark.usefixtures("driver")
    def test_last_airdrops_epoch_containers_not_empty(self, driver: WebDriver) -> None:
        """
        Verify that the Last Airdrops epoch containers list is not empty.
        :param driver: WebDriver instance
        """
        hord_page = HordPage(driver)
        with allure.step("Verify that the Last Airdrops epoch containers list is not empty"):
            assert hord_page.is_last_airdrop_epoch_containers_list_not_empty(), "Last Airdrops epoch containers should not be empty"
