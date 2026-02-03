from playwright.sync_api import expect
from pages.BasePage import BasePage
from utils.CustomLogger import get_logger


class AdminUserPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.logger = get_logger("AdminUserPage")
        self.logger.info("Initializing AdminUserPage")

        self.username_input = page.locator("(//input[@class='oxd-input oxd-input--active'])[2]")
        self.user_role_dropdown = page.locator("//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
        self.employee_name_input = page.get_by_placeholder("Type for hints...")
        self.employee_suggestion_list = page.get_by_role("option", name="Peter Mac Anderson")

        self.status_dropdown = page.locator("//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
        self.dropdown_options = page.locator("//div[@role='listbox']//span")
        self.search_button = page.locator("//button[@type='submit']")
        self.reset_button = page.locator("//button[normalize-space()='Reset']")
        # self.add_button = page.locator("//button[contains(text(), 'Add')]")
        self.results_rows = page.locator("div.oxd-table-body div.oxd-table-card")
        self.result_one_row = page.get_by_role("cell", name="Peter Anderson")
        self.no_records_message = self.page.locator("#oxd-toaster_1 p.oxd-toast-message")

        self.table_header = page.locator("div.oxd-table-header")
        # self.pagination = page.locator("//ul[@class='oxd-pagination__list']")
        self.edit_buttons = page.locator("//i[@class='oxd-icon bi-pencil-fill']")
        self.delete_buttons = page.locator("//i[@class='oxd-icon bi-trash']")
        self.confirm_delete_button = page.get_by_role("button", name="Yes, Delete")
        self.cancel_button = page.locator("//button[normalize-space()='Cancel']")
        # self.modal_title = page.locator("//h6[@class='oxd-text oxd-text--h6']")
        self.success_message = page.locator("//div[@class='oxd-toast-content']")
        self.save_button = page.locator("//button[@type='submit'][contains(text(), 'Save')]")
        self.username_field = page.locator("//label[text()='Username']/following::input[1]")

        # For add user
        self.add_button = self.page.get_by_role("button", name="Add")
        self.save_button = self.page.get_by_role("button", name="Save")

        # Dropdowns
        self.add_user_role_dropdown = self.page.get_by_label("User Role")
        self.add_status_dropdown = self.page.get_by_label("Status")

        # Inputs
        self.add_employee_name_input = self.page.get_by_placeholder("Type for hints...")
        self.add_username_input = page.get_by_text("Username", exact=True).locator("xpath=following::input[1]")

        self.add_password_input = page.get_by_text("Password", exact=True).locator("xpath=following::input[1]")

        self.add_confirm_password_input = page.get_by_text("Confirm Password", exact=True).locator("xpath=following::input[1]")

        # Job menu
        self.job_dropdown = self.page.locator("span.oxd-topbar-body-nav-tab-item",has_text="Job")
        self.job_title = page.get_by_role("menuitem", name="Job Titles")
        self.pay_grade = page.get_by_role("menuitem", name="Pay Grades")
        self.employment_status = page.get_by_role("menuitem", name="Employment Status")
        self.job_categories = page.get_by_role("menuitem", name="Job Categories")
        self.add_job_title_button =page.get_by_role("button", name="Add")


        self.job_title_input = page.get_by_text("Job Title", exact=True).locator("xpath=following::input[1]")
        self.job_description_textarea = page.get_by_placeholder("Type description here")
        self.note_textarea = page.get_by_placeholder("Add note")

        # Pay grade
        self.pay_grade_name_input = page.get_by_text("Name", exact=True).locator("xpath=following::input[1]")
        # self.min_salary_input = page.get_by_text("Minimum Salary", exact=True).locator("xpath=following::input[1]")
        self.currency_dropdown = page.locator("//label[text()='Currency']/following::div[contains(@class,'oxd-select-text')][1]")
        # self.max_salary_input = page.get_by_text("Maximum Salary", exact=True).locator("xpath=following::input[1]")
        self.add_currency_save_button = self.page.get_by_text("Add Currency", exact=True).locator("xpath=following::button[normalize-space()='Save'][1]")

        # Organization
        # General Information
        self.organization_dropdown = self.page.locator(
            "span.oxd-topbar-body-nav-tab-item",
            has_text="Organization"
        )
        self.general_information = page.get_by_role("menuitem", name="General Information")
        self.locations = page.get_by_role("menuitem", name="Locations")
        self.structure = page.get_by_role("menuitem", name="Structure")

        self.edit_general_information_button = page.get_by_label("Edit")
        self.country_dropdown = page.locator("//label[text()='Country']/following::div[contains(@class,'oxd-select-text')][1]")
        self.city_input = page.get_by_text("City", exact=True).locator("xpath=following::input[1]")

        # Qualifications
        self.qualifications_dropdown = self.page.locator(
            "span.oxd-topbar-body-nav-tab-item",
            has_text="Qualifications"
        )

        self.skills = page.get_by_role("menuitem", name="Skills")
        self.education = page.get_by_role("menuitem", name="Education")
        self.education_input = page.get_by_text("Level", exact=True).locator("xpath=following::input[1]")
        self.licenses = page.get_by_role("menuitem", name="Licenses")
        self.languages = page.get_by_role("menuitem", name="Languages")
        self.memberships = page.get_by_role("menuitem", name="Memberships")

        # Nationalities
        self.nationalities = page.get_by_text("Nationalities ", exact=True)



    def wait_for_search_results(self):
        # Wait for search results to be visible
        self.logger.info("Waiting for search results to be visible")
        expect(self.results_rows.first).to_be_visible(timeout=10000)
        self.logger.info("Search results visible")


    def select_user_role(self, role_name):
        # Click on User Role dropdown and select value
        self.logger.info(f"Selecting user role: {role_name}")
        self.user_role_dropdown.click()
        # Select required role (Admin / ESS)
        self.dropdown_options.filter(has_text=role_name).first.click()
        self.logger.info(f"User role selected: {role_name}")

    def select_status(self, status_value):
        # Click on Status dropdown and select status
        self.logger.info(f"Selecting status: {status_value}")
        self.status_dropdown.click()
        # Select required status
        self.dropdown_options.filter(has_text=status_value).first.click()
        self.logger.info(f"Status selected: {status_value}")

    def enter_username(self, username):
        # Enter username into search field
        self.logger.info(f"Entering username: {username}")
        self.username_input.fill(username)
        self.logger.info("Username entered")

    def clear_username(self):
        # Clear username input
        self.logger.info("Clearing username input")
        self.username_input.clear()
        self.logger.info("Username input cleared")

    def select_employee_name(self, employee_name):
        # Type partial employee name to trigger suggestions and select
        self.logger.info(f"Selecting employee: {employee_name}")
        self.employee_name_input.fill(employee_name)
        self.logger.info(f"Employee name entered: {employee_name}")

        option = self.employee_suggestion_list
        option.wait_for(state="visible")
        option.click()
        self.logger.info("Employee selected from suggestions")

    def clear_employee_name(self):
        # Clear employee name input field
        self.logger.info("Clearing employee name input")
        self.employee_name_input.clear()
        self.logger.info("Employee name input cleared")

    def click_search(self):
        # Click search to execute filters
        self.logger.info("Clicking search button")
        self.search_button.click()
        self.logger.info("Search clicked")

    def click_reset(self):
        # Reset search filters
        self.logger.info("Clicking reset button")
        self.reset_button.click()
        self.logger.info("Reset clicked")

    def click_add(self):
        # Click Add button to open add dialog
        self.logger.info("Clicking Add button")
        self.add_button.click()
        self.logger.info("Add dialog opened")

    def get_row_count(self):
        # Return number of result rows
        count = self.results_rows.count()
        self.logger.info(f"Number of result rows: {count}")
        return count

    def click_edit_button(self, row_index=0):
        # Click edit icon for given row
        self.logger.info(f"Clicking edit button for row: {row_index}")
        self.edit_buttons.nth(row_index).click()
        self.logger.info("Edit button clicked")

    def click_delete_button(self, row_index=0):
        # Click delete icon for given row
        self.logger.info(f"Clicking delete button for row: {row_index}")
        self.delete_buttons.nth(row_index).click()
        self.logger.info("Delete button clicked")

    def confirm_delete(self):
        # Confirm delete action in modal
        self.logger.info("Confirming delete action")
        self.confirm_delete_button.click()
        self.logger.info("Delete confirmed")

    def get_success_message(self):
        # Return success message text after operations
        self.logger.info("Waiting for success message to appear")
        expect(self.success_message).to_be_visible(timeout=5000)
        text = self.success_message.text_content()
        self.logger.info(f"Success message: {text}")
        return text

    def is_table_empty(self):
        # Check if result table has no rows
        empty = self.results_rows.count() == 0
        self.logger.info(f"Is result table empty: {empty}")
        return empty

    def add_user(self):
        # Add a new admin user with provided credentials
        self.logger.info("Starting add user flow")
        self.click_add()
        self.select_user_role("Admin")
        self.select_employee_name("Peter Mac Anderson")
        self.select_status("Enabled")
        self.add_username_input.fill("piyushkasture")
        self.add_password_input.fill("Admin@123")
        self.add_confirm_password_input.fill("Admin@123")
        self.save_button.click()
        self.logger.info("Add user submitted")

    def search_username_by_piyushkasture(self):
        # Search for specific username
        self.logger.info("Searching for username: piyushkasture")
        self.enter_username("piyushkasture")
        self.click_search()
        self.logger.info("Search by username executed")

    def edit_user(self):
        # Edit existing user and disable
        self.logger.info("Editing user to set status Disabled")
        self.click_edit_button()
        self.select_status("Disabled")
        self.save_button.click()
        self.logger.info("User edit submitted")

    def search_username_and_status(self):
        # Search by username and status
        self.logger.info("Searching by username and status: piyushkasture, Disabled")
        self.enter_username("piyushkasture")
        self.select_status("Disabled")
        self.click_search()
        self.logger.info("Search by username and status executed")

    def delete_user(self):
        # Delete a user and confirm
        self.logger.info("Deleting user")
        self.click_delete_button()
        self.confirm_delete()
        self.logger.info("User delete flow completed")
        # self.job_title_input.fill("Admin@123")
        # self.save_button.click()

# Job title
#     navigate to job title
    def go_to_job_title(self):
        # Navigate to Job Titles section
        self.logger.info("Navigating to Job Titles section")
        self.job_dropdown.click()
        self.job_title.click()
        self.logger.info("Job Titles page opened")


    def add_job_title(self):
        # Add a new job title entry
        self.logger.info("Adding new job title: Software Tester")
        self.go_to_job_title()
        self.click_add()
        self.job_title_input.fill("Software Tester")
        self.logger.info("Job title filled")
        self.job_description_textarea.fill("Software Tester role with 3 years experience")
        self.logger.info("Job description entered")
        self.save_button.click()
        self.logger.info("Job title saved")

    def edit_job_title(self):
        # Edit existing job title
        self.logger.info("Editing job title: Software Tester")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Software Tester", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.logger.info("Edit icon clicked for job title")
        self.note_textarea.fill("Demo")
        self.logger.info("Note added to job title")
        self.save_button.click()
        self.logger.info("Job title edit saved")

    def delete_job_title(self):
        # Delete a job title entry
        self.logger.info("Deleting job title: Software Tester")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Software Tester", exact=True)
        )

        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for job title")
        self.confirm_delete()
        self.logger.info("Job title deletion confirmed")

# Pay grade
    def go_to_pay_grade(self):
        # Navigate to Pay Grades section
        self.logger.info("Navigating to Pay Grades section")
        self.job_dropdown.click()
        self.pay_grade.click()
        self.logger.info("Pay Grades page opened")

    def select_currency(self):
        # Select a currency for pay grade
        self.logger.info("Selecting currency: INR - Indian Rupee")
        self.currency_dropdown.click()
        # Select required currency
        self.dropdown_options.filter(has_text="INR - Indian Rupee").first.click()
        self.logger.info("Currency selected")

    def add_pay_grade(self):
        # Add a new pay grade
        self.logger.info("Adding pay grade: Grade1234")
        self.go_to_pay_grade()
        self.click_add()
        self.pay_grade_name_input.fill("Grade1234")
        self.logger.info("Pay grade name entered")
        self.save_button.click()
        self.logger.info("Pay grade saved")

    def edit_pay_grade(self):
        # Edit pay grade and add currency
        self.logger.info("Editing pay grade: Grade1234")
        self.click_add()
        self.select_currency()
        self.add_currency_save_button.click()
        self.logger.info("Currency added to pay grade")
        self.go_to_pay_grade()
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Grade1234", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.logger.info("Pay grade edit initiated")

    def delete_pay_grade(self):
        # Delete a pay grade entry
        self.logger.info("Deleting pay grade: Grade1234")
        self.go_to_pay_grade()
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Grade1234", exact=True)
        )

        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for pay grade")
        self.confirm_delete()
        self.logger.info("Pay grade deletion confirmed")

# Employment Status
    def go_to_employment_status(self):
        # Navigate to Employment Status section
        self.logger.info("Navigating to Employment Status section")
        self.job_dropdown.click()
        self.employment_status.click()
        self.logger.info("Employment Status page opened")

    def add_employment_status(self):
        # Add a new employment status
        self.logger.info("Adding employment status: Part-Time123")
        self.go_to_employment_status()
        self.click_add()
        self.pay_grade_name_input.fill("Part-Time123")
        self.logger.info("Employment status filled")
        self.save_button.click()
        self.logger.info("Employment status saved")

    def edit_employment_status(self):
        # Edit existing employment status
        self.logger.info("Editing employment status: Part-Time123")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Part-Time123", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.logger.info("Edit icon clicked for employment status")
        self.pay_grade_name_input.click()
        self.save_button.click()
        self.logger.info("Employment status edited")

    def delete_employment_status(self):
        # Delete an employment status
        self.logger.info("Deleting employment status: Part-Time123")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Part-Time123", exact=True)
        )

        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for employment status")
        self.confirm_delete()
        self.logger.info("Employment status deletion confirmed")

# Job Categories
    def go_to_job_categories(self):
        # Navigate to Job Categories section
        self.logger.info("Navigating to Job Categories section")
        self.job_dropdown.click()
        self.job_categories.click()
        self.logger.info("Job Categories page opened")

    def add_job_categories(self):
        # Add a new job category
        self.logger.info("Adding job category: Tester")
        self.go_to_job_categories()
        self.click_add()
        self.pay_grade_name_input.fill("Tester")
        self.logger.info("Job category name entered")
        self.save_button.click()
        self.logger.info("Job category saved")

    def edit_job_categories(self):
        # Edit job category
        self.logger.info("Editing job category: Tester")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Tester", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.logger.info("Edit icon clicked for job category")
        self.pay_grade_name_input.click()
        self.save_button.click()
        self.logger.info("Job category edited")

    def delete_job_categories(self):
        # Delete job category
        self.logger.info("Deleting job category: Tester")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Tester", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for job category")
        self.confirm_delete()
        self.logger.info("Job category deletion confirmed")


# Organization
# General Information
    def go_to_general_information(self):
        # Navigate to General Information page
        self.logger.info("Navigating to General Information")
        self.organization_dropdown.click()
        self.general_information.click()
        self.logger.info("General Information page opened")

    def select_country(self):
        # Select country in general information
        self.logger.info("Selecting country: India")
        self.country_dropdown.click()
        # Select required country
        self.dropdown_options.filter(has_text="India").first.click()
        self.logger.info("Country selected: India")


    def edit_general_information(self):
        # Edit general information and save
        self.logger.info("Editing General Information")
        self.go_to_general_information()
        self.edit_general_information_button.check()
        self.logger.info("Edit enabled for general information")
        self.select_country()
        self.save_button.click()
        self.logger.info("General Information saved")

# Locations

    def go_to_location(self):
        # Navigate to Locations page
        self.logger.info("Navigating to Locations section")
        self.organization_dropdown.click()
        self.locations.click()
        self.logger.info("Locations page opened")

    def add_location(self):
        # Add a new location entry
        self.logger.info("Adding location: Pune Headquarter, Pune")
        self.go_to_location()
        self.click_add()
        self.pay_grade_name_input.fill("Pune Headquarter")
        self.city_input.fill("Pune")
        self.select_country()
        self.save_button.click()
        self.logger.info("Location saved")

    def search_location_by_name(self):
        # Search location by name
        self.logger.info("Searching for location: Pune Headquarter")
        self.pay_grade_name_input.fill("Pune Headquarter")
        self.click_search()
        self.logger.info("Location search executed")

    def edit_location(self):
        # Edit an existing location
        self.logger.info("Editing location entry")
        self.click_edit_button()
        self.save_button.click()
        self.logger.info("Location edit saved")

    def search_name_city_and_country(self):
        # Search using name, city and country filters
        self.logger.info("Searching by name, city and country: Pune Headquarter, Pune, India")
        self.pay_grade_name_input.fill("Pune Headquarter")
        self.select_country()
        self.city_input.fill("Pune")
        self.click_search()
        self.logger.info("Complex location search executed")

    def delete_location(self):
        # Delete a location entry
        self.logger.info("Deleting location")
        self.click_delete_button()
        self.confirm_delete()
        self.logger.info("Location deletion confirmed")

# Qualifications
# Skills

    def go_to_skills(self):
        # Navigate to Skills management page
        self.logger.info("Navigating to Skills section")
        self.qualifications_dropdown.click()
        self.skills.click()
        self.logger.info("Skills page opened")

    def add_skills(self):
        # Add a new skill
        self.logger.info("Adding skill: Playwright")
        self.go_to_skills()
        self.click_add()
        self.pay_grade_name_input.fill("Playwright")
        self.job_description_textarea.fill("Automation")
        self.save_button.click()
        self.logger.info("Skill saved")

    def edit_skills(self):
        # Edit an existing skill entry
        self.logger.info("Editing skill: Playwright -> Java")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Playwright", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.pay_grade_name_input.fill("Java")
        self.save_button.click()
        self.logger.info("Skill edit saved")

    def delete_skills(self):
        # Delete a skill entry
        self.logger.info("Deleting skill: Playwright")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Playwright", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for skill")
        self.confirm_delete()
        self.logger.info("Skill deletion confirmed")

# Education
    def go_to_education(self):
        # Navigate to Education section
        self.logger.info("Navigating to Education section")
        self.qualifications_dropdown.click()
        self.education.click()
        self.logger.info("Education page opened")

    def add_education(self):
        # Add a new education level
        self.logger.info("Adding education: Bachelor Degree")
        self.go_to_education()
        self.click_add()
        self.education_input.fill("Bachelor Degree")
        self.save_button.click()
        self.logger.info("Education saved")

    def edit_education(self):
        # Edit existing education entry
        self.logger.info("Editing education: Bachelor Degree")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Bachelor Degree", exact=True))
        row.locator("i.bi-pencil-fill").click()
        # self.pay_grade_name_input.click()
        self.save_button.click()
        self.logger.info("Education edit saved")

    def delete_education(self):
        # Delete an education entry
        self.logger.info("Deleting education: Bachelor Degree")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Bachelor Degree", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for education")
        self.confirm_delete()
        self.logger.info("Education deletion confirmed")

# Licenses
    def go_to_licenses(self):
        # Navigate to Licenses section
        self.logger.info("Navigating to Licenses section")
        self.qualifications_dropdown.click()
        self.licenses.click()
        self.logger.info("Licenses page opened")

    def add_licenses(self):
        # Add a new license
        self.logger.info("Adding license: Certificate in Automation Testing")
        self.go_to_licenses()
        self.click_add()
        self.pay_grade_name_input.fill("Certificate in Automation Testing")
        self.save_button.click()
        self.logger.info("License saved")

    def edit_licenses(self):
        # Edit existing license
        self.logger.info("Editing license: Certificate in Automation Testing")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Certificate in Automation Testing", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.pay_grade_name_input.click()
        self.save_button.click()
        self.logger.info("License edit saved")

    def delete_licenses(self):
        # Delete a license entry
        self.logger.info("Deleting license: Certificate in Automation Testing")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Certificate in Automation Testing", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for license")
        self.confirm_delete()
        self.logger.info("License deletion confirmed")

# Languages
    def go_to_languages(self):
        # Navigate to Languages section
        self.logger.info("Navigating to Languages section")
        self.qualifications_dropdown.click()
        self.languages.click()
        self.logger.info("Languages page opened")

    def add_languages(self):
        # Add a new language
        self.logger.info("Adding language: Marathi")
        self.go_to_languages()
        self.click_add()
        self.pay_grade_name_input.fill("Marathi")
        self.save_button.click()
        self.logger.info("Language saved")

    def edit_languages(self):
        # Edit existing language entry
        self.logger.info("Editing language: Marathi -> Hindi")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Marathi", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.pay_grade_name_input.fill("Hindi")
        self.save_button.click()
        self.logger.info("Language edit saved")

    def delete_languages(self):
        # Delete a language entry
        self.logger.info("Deleting language: Marathi")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Marathi", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for language")
        self.confirm_delete()
        self.logger.info("Language deletion confirmed")

# Memberships
    def go_to_memberships(self):
        # Navigate to Memberships section
        self.logger.info("Navigating to Memberships section")
        self.qualifications_dropdown.click()
        self.memberships.click()
        self.logger.info("Memberships page opened")

    def add_memberships(self):
        # Add a membership
        self.logger.info("Adding membership: CDAC")
        self.go_to_memberships()
        self.click_add()
        self.pay_grade_name_input.fill("CDAC")
        self.save_button.click()
        self.logger.info("Membership saved")

    def edit_memberships(self):
        # Edit existing membership
        self.logger.info("Editing membership: CDAC")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("CDAC", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.pay_grade_name_input.fill("Hindi")
        self.save_button.click()
        self.logger.info("Membership edit saved")

    def delete_memberships(self):
        # Delete a membership
        self.logger.info("Deleting membership: CDAC")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("CDAC", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for membership")
        self.confirm_delete()
        self.logger.info("Membership deletion confirmed")

# Nationalities
    def go_to_nationalities(self):
        # Navigate to Nationalities section
        self.logger.info("Navigating to Nationalities section")
        self.nationalities.click()
        self.logger.info("Nationalities page opened")

    def add_nationalities(self):
        # Add a nationality
        self.logger.info("Adding nationality: American-Indian")
        self.go_to_nationalities()
        self.click_add()
        self.pay_grade_name_input.fill("American-Indian")
        self.save_button.click()
        self.logger.info("Nationality saved")

    def edit_nationalities(self):
        # Edit a nationality entry
        self.logger.info("Editing nationality: American-Indian")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("American-Indian", exact=True))
        row.locator("i.bi-pencil-fill").click()
        self.pay_grade_name_input.click()
        self.save_button.click()
        self.logger.info("Nationality edit saved")

    def delete_nationalities(self):
        # Delete a nationality
        self.logger.info("Deleting nationality: American-Indian")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("American-Indian", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.logger.info("Delete icon clicked for nationality")
        self.confirm_delete()
        self.logger.info("Nationality deletion confirmed")