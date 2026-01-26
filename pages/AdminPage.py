from logging import Logger
from playwright.sync_api import Page, expect
from pages.BasePage import BasePage

class AdminUserPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.username_input = page.locator("(//input[@class='oxd-input oxd-input--active'])[2]")
        self.user_role_dropdown = page.locator("//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
        self.dropdown_options = page.locator("//div[@role='listbox']//span")
        self.search_button = page.locator("//button[@type='submit']")
        self.results_rows = page.locator("div.oxd-table-body div.oxd-table-card")
        self.no_records = page.locator("span:has-text('No Records Found')")

    def wait_for_search_results(self):
        expect(self.results_rows.first).to_be_visible(timeout=10000)
    def select_user_role(self, role_name):
        # Click on User Role dropdown
        self.user_role_dropdown.click()

        # Select required role (Admin / ESS)
        self.dropdown_options.filter(has_text=role_name).first.click()


