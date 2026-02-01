from playwright.sync_api import Page
from pages.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #Locators

        self.logout_button = page.get_by_role("menuitem", name="Logout")



    #Methods
    def click_logout_button(self):
        self.logout_button.click()