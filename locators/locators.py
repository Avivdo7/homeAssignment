from selenium.webdriver.common.by import By


# Hord Page Locators

class HordPageLocators:
    # XPATH constants
    FAQ_QUESTION_FOLLOWING_SIBLING = "/following-sibling::div[@class='pointer']/div"

    # Sidebar locators
    SIDEBAR: tuple[By, str] = (By.XPATH, "//aside[contains(@class, 'duf-aside')]")
    TOGGLE_SIDEBAR_BUTTON: tuple[By, str] = (By.XPATH, "//div[contains(@class, 'side-bar-toggler')]")

    # FAQ section locators
    FAQ_SECTION_HEADER: tuple[By, str] = (By.XPATH, "//h2[contains(text(),'Frequently Asked Questions')]")
    FAQ_ETH_STAKING: tuple[By, str] = (By.XPATH, "//span[contains(text(),'What is ETH staking?')]")
    FAQ_HORD_REWARDS: tuple[By, str] = (By.XPATH, "//span[contains(text(),'What are HORD rewards?')]")
    POINTER_FAQ_ETH_STAKING: tuple[By, str] = (By.XPATH, FAQ_ETH_STAKING[1] + FAQ_QUESTION_FOLLOWING_SIBLING)
    POINTER_FAQ_HORD_REWARDS: tuple[By, str] = (By.XPATH, FAQ_HORD_REWARDS[1] + FAQ_QUESTION_FOLLOWING_SIBLING)
    FAQ_ETH_STAKING_ANSWER: tuple[By, str] = (By.XPATH,
                                              "//*[contains(text(),'ETH staking is a process in which ETH holders can use their ETH to power the Ethereum blockchain and earn rewards in the process.')]")

    # Revenue Share section locators
    REVENUE_SHARE_LINK: tuple[By, str] = (By.XPATH, "//a[@href='/revenue-share']")
    REVENUE_SHARE_HEADER: tuple[By, str] = (By.XPATH, "//h2[contains(text(), 'Revenue Share')]")

    # Last Airdrops locators
    LAST_AIRDROPS_HEADER: tuple[By, str] = (By.XPATH, "//h2[contains(text(), 'Last Airdrops')]")
    LAST_AIRDROPS_EPOCH: tuple[By, str] = (By.XPATH, "//*[contains(@class, 'epoch-container')]")
