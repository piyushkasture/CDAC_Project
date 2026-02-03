from playwright.sync_api import Page
from pages.BasePage import BasePage
from utils.CustomLogger import get_logger


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = get_logger("ProfilePage")
        self.logger.info("Initializing ProfilePage")

        #Locators
        self.logout_button = page.get_by_role("menuitem", name="Logout")

    #Methods
    def click_logout_button(self):
        # Click logout button
        self.logger.info("Clicking logout button")
        self.logout_button.click()
        self.logger.info("Logout")