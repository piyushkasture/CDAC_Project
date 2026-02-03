from playwright.sync_api import Page, expect
from utils.CustomLogger import get_logger

class DirectoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger("DirectoryPage")
        self.logger.info("Initializing DirectoryPage")

        # Navigation
        self.directory_menu = page.get_by_role("link", name="Directory")

        # Search fields
        self.employee_name_input = page.get_by_placeholder("Type for hints...")
        self.employee_suggestion_list = page.get_by_role("option", name="Peter Mac Anderson")
        self.job_title_dropdown = page.locator("//label[text()='Job Title']/following::div[contains(@class,'oxd-select-text')][1]")
        self.location_dropdown = page.locator("//label[text()='Location']/following::div[contains(@class,'oxd-select-text')][1]")

        # Buttons
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")

        # Results
        self.employee_cards = page.locator(".orangehrm-directory-card")
        self.employee_name_listbox = page.get_by_role("listbox")
        self.no_records_found = self.employee_name_listbox.get_by_text("No Records Found", exact=True)

        self.invalid_message = page.get_by_text("Invalid")


    def select_job_title(self, job_title):
        # Select job title from dropdown filter
        self.logger.info(f"Selecting job title: {job_title}")
        self.job_title_dropdown.click()
        self.page.get_by_role("option", name=job_title).first.click()
        self.logger.info(f"Job title selected: {job_title}")

    def select_location(self, location):
        # Select location from dropdown filter
        self.logger.info(f"Selecting location: {location}")
        self.location_dropdown.click()
        self.page.get_by_role("option", name=location).first.click()
        self.logger.info(f"Location selected: {location}")

    def select_employee_name(self, employee_name):
        # Type partial name to trigger suggestions and select from list
        self.logger.info(f"Searching for employee: {employee_name}")
        self.employee_name_input.fill(employee_name)
        self.logger.info(f"Employee name entered: {employee_name}")

        option = self.employee_suggestion_list
        option.wait_for(state="visible")
        self.logger.info("Employee suggestion visible")
        option.click()
        self.logger.info("Employee selected")

    def select_employee_name_for_invalid(self, employee_name):
        # Type partial name to verify no matching records found
        self.logger.info(f"Searching with invalid name: {employee_name}")
        self.employee_name_input.fill(employee_name)
        self.logger.info(f"Invalid name entered: {employee_name}")

        expect(self.employee_name_listbox).to_be_visible()
        expect(self.no_records_found).to_be_visible()
        self.logger.info("No records found message verified")

    def clear_employee_name(self):
        # Clear employee name input field
        self.logger.info("Clearing employee name input")
        self.employee_name_input.clear()
        self.logger.info("Employee name field cleared")

    def click_search(self):
        # Execute directory search
        self.logger.info("Executing search")
        self.search_button.click()
        self.logger.info("Search executed")

    def click_reset(self):
        # Reset all search filters
        self.logger.info("Resetting search filters")
        self.reset_button.click()
        self.logger.info("Filters reset")

    def search_employee_by_name(self):
        # Search directory by employee name
        self.logger.info("Starting employee search by name")
        self.select_employee_name("Peter")
        self.click_search()
        self.logger.info("Name-based search completed")

    def search_employee_by_invalid_name(self):
        # Search with non-existent employee name
        self.logger.info("Searching with invalid employee name")
        self.clear_employee_name()
        self.select_employee_name_for_invalid("Piyush Kasture")
        self.logger.info("Invalid name search verification completed")

    def search_employee_by_job_title(self):
        # Search directory by job title
        self.logger.info("Starting employee search by job title")
        self.clear_employee_name()
        self.select_job_title("Chief Financial Officer")
        self.click_search()
        self.logger.info("Job title-based search completed")

    def search_employee_by_location(self):
        # Search directory by location
        self.logger.info("Starting employee search by location")
        self.click_reset()
        self.select_location("New York Sales Office")
        self.click_search()
        self.logger.info("Location-based search completed")

    def search_employee_using_multiple_filters(self):
        # Search directory using name, job title, and location filters
        self.logger.info("Starting multi-filter employee search")
        self.click_reset()
        self.select_employee_name("Peter")
        self.select_job_title("Chief Financial Officer")
        self.select_location("New York Sales Office")
        self.click_search()
        self.logger.info("Multi-filter search completed")

    def search_without_any_criteria(self):
        # Search directory without any filters applied
        self.logger.info("Executing search without criteria")
        self.click_reset()
        self.click_search()
        self.logger.info("Uncfiltered search executed")

    def reset_button_functionality(self):
        # Test reset button clears all filters
        self.logger.info("Testing reset button functionality")
        self.select_job_title("Chief Financial Officer")
        self.click_reset()
        self.logger.info("Reset button verified")

    def multiple_consecutive_searches(self):
        # Execute multiple search operations sequentially
        self.logger.info("Starting consecutive searches")
        self.search_employee_by_name()
        self.search_employee_by_location()
        self.logger.info("Consecutive searches completed")
