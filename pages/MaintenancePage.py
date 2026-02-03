from playwright.sync_api import Page, expect
from utils.CustomLogger import get_logger


class MaintenancePage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger("MaintenancePage")
        self.logger.info("Initializing MaintenancePage")

        # Password confirmation
        self.password_input = page.locator("div.oxd-input-group:has-text('Password') input")
        self.confirm_button = page.get_by_role("button", name="Confirm")

        # Tabs
        self.purge_records_dropdown = self.page.locator("span.oxd-topbar-body-nav-tab-item", has_text="Purge Records")
        self.candidate_records = page.get_by_role("menuitem", name="Candidate Records")
        # self.candidate_records_tab = page.get_by_role("tab", name="Candidate Records")

        # Search
        self.employee_name_input = page.get_by_placeholder("Type for hints...")
        self.employee_suggestion_list = page.get_by_role("option", name="Peter Mac Anderson")
        self.vacancy_suggestion_list = page.get_by_role("option", name="Senior QA Lead")
        self.employee_name_listbox = page.get_by_role("listbox")
        self.search_button = page.get_by_role("button", name="Search")

        # Purge actions
        self.purge_button = page.get_by_role("button", name="Purge")
        self.confirm_purge_button = page.get_by_role("button", name="Yes, Purge")
        self.cancel_button = page.get_by_role("button", name="Cancel")

        # Messages
        self.error_message = page.locator(".oxd-alert-content-text")
        self.required_message = page.locator(".oxd-input-field-error-message")
        self.landing_page_heading = page.get_by_role("heading", name="Purge Employee Records")
        self.landing_candidate_page_heading = page.get_by_role("heading", name="Purge Candidate Records")
        self.vacancy_card = page.locator(".oxd-table-card")

        # Directory-style autocomplete / empty state
        self.no_records_found = page.get_by_text("No Records Found", exact=True)

    def open_maintenance_with_valid_password(self):
        # Open maintenance module with valid password
        self.logger.info("Opening maintenance with valid password")
        self.password_input.fill("admin123")
        self.logger.info("Password entered")
        self.confirm_button.click()
        self.logger.info("Maintenance access confirmed")

    def open_candidate_records(self):
        # Navigate to Candidate Records section
        self.logger.info("Opening Candidate Records section")
        self.purge_records_dropdown.click()
        self.logger.info("Purge Records dropdown clicked")
        self.candidate_records.click()
        self.logger.info("Candidate Records tab opened")

    def search_record(self, name):
        # Search for employee/candidate record by name
        self.logger.info(f"Searching for record: {name}")
        self.employee_name_input.fill(name)
        self.logger.info(f"Name entered: {name}")
        self.search_button.click()
        self.logger.info("Search executed")

    def purge_record(self):
        # Initiate and confirm purge action
        self.logger.info("Initiating record purge")
        self.purge_button.click()
        self.logger.info("Purge button clicked")
        self.confirm_purge_button.click()
        self.logger.info("Purge confirmed")

    def cancel_purge(self):
        # Cancel the purge operation
        self.logger.info("Canceling purge operation")
        self.purge_button.click()
        self.logger.info("Purge button clicked")
        self.cancel_button.click()
        self.logger.info("Purge cancelled")

    def open_maintenance_with_invalid_password(self):
        # Attempt to open maintenance with invalid password
        self.logger.info("Attempting maintenance access with invalid password")
        self.password_input.fill("piyushkasture")
        self.logger.info("Invalid password entered")
        self.confirm_button.click()
        self.logger.info("Invalid password submission attempted")

    def open_maintenance_with_black_password(self):
        # Attempt to open maintenance with blank password
        self.logger.info("Attempting maintenance access with blank password")
        self.password_input.fill("")
        self.logger.info("Blank password submitted")
        self.confirm_button.click()
        self.logger.info("Blank password submission attempted")

    def search_with_invalid_name(self, name):
        # Search with invalid/non-existent name
        self.logger.info(f"Searching with invalid name: {name}")
        self.employee_name_input.fill(name)
        self.logger.info(f"Invalid name entered: {name}")
        self.search_button.click()
        self.logger.info("Search with invalid name executed")

    def select_employee_name_for_invalid(self, employee_name):
        # Type partial name to trigger suggestions and verify no records
        self.logger.info(f"Entering partial name for search: {employee_name}")
        self.employee_name_input.fill(employee_name)
        self.logger.info(f"Partial name entered: {employee_name}")

        expect(self.employee_name_listbox).to_be_visible()
        self.logger.info("Listbox visible but no matching records")
        expect(self.no_records_found).to_be_visible()
        self.logger.info("No records found message verified")

    def attempt_purge_without_selection(self):
        # Attempt to purge without selecting a record
        self.logger.info("Attempting purge without record selection")
        self.purge_button.click()
        self.logger.info("Purge button clicked without selection")

    def search_past_employee_records(self):
        # Search for past/deleted employee records
        self.logger.info("Searching for past employee records")
        self.select_employee_name_for_invalid("Peter")
        self.logger.info("Past employee records search completed")

    def select_vacancy_name(self, vacancy_name):
        # Type partial vacancy name to trigger suggestions and select from list
        self.logger.info(f"Searching for vacancy: {vacancy_name}")
        self.employee_name_input.fill(vacancy_name)
        self.logger.info(f"Vacancy name entered: {vacancy_name}")

        option = self.vacancy_suggestion_list
        option.wait_for(state="visible")
        self.logger.info("Vacancy option visible")
        option.click()
        self.logger.info("Vacancy selected")

    def search_candidate_records(self):
        # Search for candidate records by vacancy name
        self.logger.info("Starting candidate records search")
        self.select_vacancy_name("Senior QA Lead")
        self.logger.info("Vacancy selected, executing search")
        self.search_button.click()
        self.logger.info("Candidate records search completed")

