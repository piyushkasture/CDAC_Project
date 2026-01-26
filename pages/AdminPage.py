from logging import Logger
from playwright.sync_api import Page, expect
from pages.BasePage import BasePage

class AdminUserPage(BasePage):
    # def __init__(self, page: Page, logger=None):
    #     super().__init__(page)
    #     self.logger = logger
    #
    #     # Locators
    #     self.username_input = page.locator("(//input[@class='oxd-input oxd-input--active'])[2]")
    #     # User role dropdown locator for selecting user roles
    #     self.user_role_dropdown = page.locator("(//div[@class='oxd-select-wrapper'])[1]")
    #     self.search_button = page.locator("//button[@type='submit']")
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.user_role_dropdown = "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]"
        self.dropdown_options = "//div[@role='listbox']//span"
        self.results_rows = "div.oxd-table-body div.oxd-table-card"
        self.no_records = "span:has-text('No Records Found')"

    def wait_for_search_results(self):
        expect(
            self.page.locator(self.results_rows).first
        ).to_be_visible(timeout=10000)

    def select_user_role(self, role_name: str):
        # Click on User Role dropdown
        self.page.click(self.user_role_dropdown)

        # Select required role (Admin / ESS)
        self.page.locator(self.dropdown_options).filter(
            has_text=role_name
        ).first.click()


