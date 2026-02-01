from playwright.sync_api import Page

class MaintenancePage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.maintenance_menu = page.locator("a[href*='maintenance']")
        self.password_input = page.locator("input[type='password']")
        self.confirm_button = page.locator("button:has-text('Confirm')")

        self.employee_records_tab = page.locator("text=Employee Records")
        self.candidate_records_tab = page.locator("text=Candidate Records")

        self.employee_name_input = page.locator("input[placeholder='Type for hints']")
        self.search_button = page.locator("button:has-text('Search')")
        self.purge_button = page.locator("button:has-text('Purge')")
        self.confirm_purge_button = page.locator("button:has-text('Yes, Purge')")
        self.cancel_button = page.locator("button:has-text('Cancel')")

        # Error / validation locators
        self.error_message = page.locator(".oxd-alert-content-text")
        self.no_records_found = page.locator("text=No Records Found")

    def open_maintenance(self, password: str):
        self.maintenance_menu.click()
        self.password_input.fill(password)
        self.confirm_button.click()

    def open_employee_records(self):
        self.employee_records_tab.click()

    def open_candidate_records(self):
        self.candidate_records_tab.click()

    def search_record(self, name: str):
        self.employee_name_input.fill(name)
        self.search_button.click()

    def purge_record(self):
        self.purge_button.click()
        self.confirm_purge_button.click()

    def cancel_purge(self):
        self.purge_button.click()
        self.cancel_button.click()

    def open_maintenance_with_invalid_password(self, password: str):
        self.maintenance_menu.click()
        self.password_input.fill(password)
        self.confirm_button.click()

    def search_with_invalid_name(self, name: str):
        self.employee_name_input.fill(name)
        self.search_button.click()

    def attempt_purge_without_selection(self):
        self.purge_button.click()
