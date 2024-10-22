from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import HordPageLocators
from utils.utils import is_element_present, click_element, wait_for_element


class HordPage:
    """
    Page Object Model (POM) for the Hord staging application.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def sidebar(self):
        """
        Dynamically locate the sidebar element.
        :return: The sidebar WebElement
        """
        return self.driver.find_element(*HordPageLocators.SIDEBAR)

    @property
    def toggle_button(self):
        """
        Dynamically locate the toggle button element.
        :return: The toggle button WebElement
        """
        return self.driver.find_element(*HordPageLocators.TOGGLE_SIDEBAR_BUTTON)

    @property
    def pointer_faq_eth(self):
        """
        Dynamically locate the ETH staking FAQ element.
        :return: The pointer FAQ ETH WebElement
        """
        return self.driver.find_element(*HordPageLocators.POINTER_FAQ_ETH_STAKING)

    @property
    def last_airdrop_epoch_containers(self):
        """
        Dynamically locate the last airdrops epoch container elements.
        :return: A list of WebElements for the last airdrop epochs
        """
        return self.driver.find_elements(*HordPageLocators.LAST_AIRDROPS_EPOCH)

    @property
    def is_sidebar_collapsed(self) -> bool:
        """
        Check whether the sidebar is collapsed by evaluating its CSS class.
        :return: True if the sidebar is collapsed, False otherwise
        """
        sidebar_class = self.sidebar.get_attribute("class")
        return "sidebar-expanded" not in sidebar_class

    def click_toggle_button_with_js(self) -> None:
        """
        Use JavaScript to click the toggle button to collapse or expand the sidebar.
        """
        click_element(self.driver, self.toggle_button)


    def is_faq_section_exists(self) -> bool:
        """
        Verify if the FAQ section is present on the page.
        :return: True if the FAQ section exists, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.FAQ_SECTION_HEADER)

    def is_faq_eth_exists(self) -> bool:
        """
        Verify if the ETH staking question in the FAQ section is present.
        :return: True if the ETH staking question is present, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.FAQ_ETH_STAKING)

    def is_faq_eth_answer_exists(self) -> bool:
        """
        Verify if the answer for the ETH staking question is present.
        :return: True if the answer for the ETH staking question is present, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.FAQ_ETH_STAKING_ANSWER)

    def is_faq_eth_question_open(self) -> bool:
        """
        Check whether the ETH staking question is open (expanded).
        :return: True if the question is expanded, False otherwise
        """
        faq_eth_question_class = self.pointer_faq_eth.get_attribute("class")
        return "toggled" in faq_eth_question_class

    def is_last_airdrops_section_exists(self) -> bool:
        """
        Verify if the Last Airdrops section is present on the page.
        :return: True if the Last Airdrops section exists, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.LAST_AIRDROPS_HEADER)

    def is_last_airdrop_epoch_containers_list_not_empty(self) -> bool:
        """
        Check whether the Last Airdrops epoch container list is not empty.
        :return: True if the list contains elements, False otherwise
        """
        return bool(self.last_airdrop_epoch_containers)
