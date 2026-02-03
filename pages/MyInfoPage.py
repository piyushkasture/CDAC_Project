from playwright.sync_api import Page, expect
from pages.BasePage import BasePage

class MyInfoPage(BasePage):

    def __init__(self, page: Page, logger=None):
        super().__init__(page, logger)
        # Common locators (Playwright only)
        self.save_button = page.get_by_role("button", name="Save")
        self.edit_buttons = page.locator("//i[@class='oxd-icon bi-pencil-fill']")
        self.delete_buttons = page.locator("//i[@class='oxd-icon bi-trash']")
        self.confirm_delete_button = page.get_by_role("button", name="Yes, Delete")
        # self.edit_button = self.page.get_by_role("button", name="Edit")

        # self.delete_icons = page.locator("i.bi-trash")
        self.success_toast = page.locator("div.oxd-toast-content")
        self.no_records = page.get_by_text("No Records Found")

        # Personal Info
        self.first_name = page.get_by_placeholder("First Name")
        self.middle_name = page.get_by_placeholder("Middle Name")
        self.last_name = page.get_by_placeholder("Last Name")

        # file Attachment
        self.file_input = page.get_by_text("Select File", exact=True).locator("xpath=following::input[1]")
        # Comment textarea
        self.comment_input = page.get_by_placeholder("Type comment here")
        # Save button (scoped inside Add Attachment section)
        self.attachment_save_button = page.get_by_text("Add Attachment", exact=True).locator("xpath=following::button[normalize-space()='Save'][1]")
        # Success toast
        self.attachment_success_toast = page.get_by_text("Successfully Saved", exact=True)

        # Contact
        self.mobile_input_field = page.locator("label:has-text('Mobile')").locator("xpath=following::input[1]")
        self.work_email_field = page.locator("label:has-text('Work Email')").locator("xpath=following::input[1]")
        self.street1_input_field = page.locator("label:has-text('Street 1')").locator("xpath=following::input[1]")

        # Emergency Contacts
        self.emergency_add_button = page.get_by_text("Assigned Emergency Contacts", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.name_input_field = page.locator("label:has-text('Name')").locator("xpath=following::input[1]")
        self.relationship_input_field = page.locator("label:has-text('Relationship')").locator("xpath=following::input[1]")
        self.home_number_input_field = page.locator("label:has-text('Home Telephone')").locator("xpath=following::input[1]")

        # Dependents
        self.dependent_add_button = page.get_by_text("Assigned Dependents", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.relationship_dropdown = page.locator("//label[text()='Relationship']/following::div[contains(@class,'oxd-select-text')][1]")
        self.dropdown_options = page.locator("//div[@role='listbox']//span")
        self.dob_input_field = page.locator("label:has-text('Date of Birth')").locator("xpath=following::input[1]")

        # Immigration
        self.immigration_add_button = page.get_by_text("Assigned Immigration Records", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.number_input_field = page.locator("label:has-text('Number')").locator("xpath=following::input[1]")
        self.issue_date_input_field = page.locator("label:has-text('Issued Date')").locator("xpath=following::input[1]")
        self.expiry_date_input_field = page.locator("label:has-text('Expiry Date')").locator("xpath=following::input[1]")
        self.eligible_status_input_field = page.locator("label:has-text('Eligible Status')").locator("xpath=following::input[1]")
        self.issued_by_dropdown = page.locator("//label[text()='Issued By']/following::div[contains(@class,'oxd-select-text')][1]")

        # Job
        self.job_heading = page.get_by_role("heading", name="Job Details").or_(page.get_by_text("Job Details"))

        #Salary
        self.salary_heading = page.get_by_role("heading", name="Assigned Salary Components").or_(page.get_by_text("Assigned Salary Components"))

        # Report-to
        self.report_to_heading = page.get_by_role("heading", name="Report to").or_(page.get_by_text("Report to"))

        # Qualification Work experiance
        self.work_experiance_add_button = page.get_by_text("Work Experience", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.education_add_button = page.get_by_text("Education", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.skills_add_button = page.get_by_text("Skills", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.languages_add_button = page.get_by_text("Languages", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.licence_add_button = page.get_by_text("License", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")

        self.company_input_field = page.locator("label:has-text('Company')").locator("xpath=following::input[1]")
        self.job_title_input_field = page.locator("label:has-text('Job Title')").locator("xpath=following::input[1]")
        self.from_input_field = page.locator("label:has-text('From')").locator("xpath=following::input[1]")
        self.to_input_field = page.locator("label:has-text('To')").locator("xpath=following::input[1]")

        # Education
        self.level_dropdown = page.locator("//label[text()='Level']/following::div[contains(@class,'oxd-select-text')][1]")
        self.year_input_field = page.locator("label:has-text('Year')").locator("xpath=following::input[1]")
        self.institute_input_field = page.locator("label:has-text('Institute')").locator("xpath=following::input[1]")

        # Skills
        self.skills_dropdown = page.locator("//label[text()='Skill']/following::div[contains(@class,'oxd-select-text')][1]")
        self.year_experiance_input_field = page.locator("label:has-text('Years of Experience')").locator("xpath=following::input[1]")

        # Language
        self.language_dropdown = page.locator("//label[text()='Language']/following::div[contains(@class,'oxd-select-text')][1]")
        self.fluency_dropdown = page.locator("//label[text()='Fluency']/following::div[contains(@class,'oxd-select-text')][1]")
        self.competency_dropdown = page.locator("//label[text()='Competency']/following::div[contains(@class,'oxd-select-text')][1]")

        # Membership
        self.membership_add_button = page.get_by_text("Assigned Memberships", exact=True).locator("xpath=following::button[.//text()[contains(., 'Add')]][1]")
        self.membership_dropdown = page.locator("//label[text()='Membership']/following::div[contains(@class,'oxd-select-text')][1]")
        self.subscription_paid_by_dropdown = page.locator("//label[text()='Subscription Paid By']/following::div[contains(@class,'oxd-select-text')][1]")
        self.amount_input_field = page.locator("label:has-text('Subscription Amount')").locator("xpath=following::input[1]")


    def open_tab(self, tab_name: str):
        # Open a My Info tab by exact link text
        self.logger.info(f"Opening tab: {tab_name}")
        self.page.get_by_role("link", name=tab_name).click()
        self.page.wait_for_load_state("networkidle")
        self.logger.info(f"{tab_name} tab loaded successfully")

    def open_personal_details(self):
        self.open_tab("Personal Details")

    def open_contact_details(self):
        self.open_tab("Contact Details")

    def open_emergency_contacts(self):
        self.open_tab("Emergency Contacts")

    def open_dependents(self):
        self.open_tab("Dependents")

    def open_immigration(self):
        self.open_tab("Immigration")

    def open_job(self):
        self.open_tab("Job")

    def open_salary(self):
        self.open_tab("Salary")

    def open_report_to(self):
        self.open_tab("Report-to")

    def open_qualifications(self):
        self.open_tab("Qualifications")


    def open_memberships(self):
        self.open_tab("Memberships")

    def wait_for_success_toast(self, timeout: int = 5000):
        # Wait for success toast (Successfully Updated/Saved/Deleted).
        expect(self.success_toast).to_be_visible(timeout=timeout)
        self.logger.info("Success toast visible")

    def click_edit_button(self, row_index=0):
        self.edit_buttons.nth(row_index).click()

    def click_delete_button(self, row_index=0):
        self.delete_buttons.nth(row_index).click()

    def confirm_delete(self):
        self.confirm_delete_button.click()


    def click_save(self):
        # Click the primary Save button on the form
        self.logger.info("Clicking Save button")
        self.save_button.click()
        self.logger.info("Save action completed")

    def click_emergency_add(self):
        # Click Add button for emergency contacts
        self.logger.info("Opening Add Emergency Contact dialog")
        emergency_add = self.emergency_add_button
        expect(emergency_add).to_be_visible()
        emergency_add.click()
        self.logger.info("Emergency Add button clicked")

    def update_personal(self, get_my_info_data):
        # Update personal details with first, middle, and last name
        self.logger.info("Updating personal details")
        self.first_name.click()
        self.first_name.clear()
        self.first_name.fill(get_my_info_data["personal"]["data1"]["first"])
        self.logger.info(f"First name filled: {get_my_info_data['personal']['data1']['first']}")
        self.middle_name.click()
        self.middle_name.clear()
        self.middle_name.fill(get_my_info_data["personal"]["data1"]["middle"])
        self.logger.info(f"Middle name filled: {get_my_info_data['personal']['data1']['middle']}")
        self.last_name.click()
        self.last_name.clear()
        self.last_name.fill(get_my_info_data["personal"]["data1"]["last"])
        self.logger.info(f"Last name filled: {get_my_info_data['personal']['data1']['last']}")
        self.save_button.click()
        self.logger.info("Personal details saved")

    def add_attachment(self):
        # Upload file with comment
        self.logger.info("Starting attachment upload")
        self.file_input.set_input_files("utils\\TestImage.jpg")
        self.logger.info("File selected for upload")
        self.comment_input.fill("Test image")
        self.logger.info("Comment added to attachment")
        self.save_button.click()
        self.logger.info("Attachment saved")



    def get_first_name_input(self):
        return self.page.get_by_placeholder("First Name").first

    def get_middle_name_input(self):
        return self.page.get_by_placeholder("Middle Name").first

    def get_last_name_input(self):
        return self.page.get_by_placeholder("Last Name").first

    def get_nickname_input(self):
        return self.page.get_by_placeholder("Nickname").first

    def get_employee_id_input(self):
        return self.page.locator("input[name='employeeId']").first


    def is_personal_details_visible(self) -> bool:
        try:
            expect(self.get_first_name_input()).to_be_visible(timeout=3000)
            return True
        except Exception:
            return False

    #  Contact Details (edit only)


    def get_mobile_input(self):
        return self.page.get_by_placeholder("Mobile").first

    def get_work_email_input(self):
        return self.page.get_by_placeholder("Work Email").first

    def get_street1_input(self):
        return self.page.get_by_placeholder("Street 1").first

    def update_mobile(self, number: str):
        self.get_mobile_input().fill(number)
        self.click_save()

    def update_email(self, email: str):
        self.get_work_email_input().fill(email)
        self.click_save()

    def update_contact(self, mobile: str, email: str, street1: str = None):
        # Contact Details page is editable by default
        # Mobile
        mobile_input = self.mobile_input_field
        expect(mobile_input).to_be_visible()
        mobile_input.fill(mobile)

        # Work Email
        work_email = self.work_email_field
        expect(work_email).to_be_visible()
        work_email.fill(email)

        # Street 1 (optional)
        if street1:
            street1_input = self.street1_input_field
            expect(street1_input).to_be_visible()
            street1_input.fill(street1)

        # Save
        self.save_button.first.click()

        # Assert success toast
        expect(self.page.get_by_text("Successfully Updated")).to_be_visible()

    #  Emergency Contacts (create → edit → delete)

    def add_emergency_contact(self, name: str, relationship: str, home_phone: str):
        # Add emergency contact with name, relationship, and phone
        self.logger.info(f"Adding emergency contact: {name}")

        # Click correct Add button (Emergency Contacts section only)
        self.click_emergency_add()

        # Scope to OrangeHRM drawer/form
        name_field= self.name_input_field
        expect(name_field).to_be_visible()
        name_field.fill(name)
        self.logger.info(f"Emergency contact name filled: {name}")

        relationship_field = self.relationship_input_field
        expect(relationship_field).to_be_visible()
        relationship_field.fill(relationship)
        self.logger.info(f"Relationship filled: {relationship}")

        home_number_field = self.home_number_input_field
        expect(home_number_field).to_be_visible()
        home_number_field.fill(home_phone)
        self.logger.info(f"Home phone filled: {home_phone}")

        self.save_button.first.click()
        self.logger.info("Emergency contact saved")
        # Assert success toast
        expect(self.page.get_by_text("Successfully Saved")).to_be_visible()

    def edit_emergency_contact(self):
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("One", exact=True))
        row.locator("i.bi-pencil-fill").click()
        name_field = self.name_input_field
        name_field.click()
        self.save_button.click()

    def delete_emergency_contact(self):
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("One", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.confirm_delete()

    def has_emergency_contact_rows(self) -> bool:
        return self.edit_buttons.count() > 0

    #  Dependents 

    def select_relationship(self):
        # Click on dropdown
        self.relationship_dropdown.click()
        # Select Child
        self.dropdown_options.filter(has_text="Child").first.click()

    def add_dependent(self, name, dob):
        # Add dependent with name and date of birth
        self.logger.info(f"Adding dependent: {name} with DOB: {dob}")
        self.dependent_add_button.first.click()
        self.logger.info("Dependent Add button clicked")
        name_field = self.name_input_field
        expect(name_field).to_be_visible()
        name_field.fill(name)
        self.logger.info(f"Dependent name filled: {name}")

        dob_field = self.dob_input_field
        expect(dob_field).to_be_visible()
        dob_field.fill(dob)
        self.logger.info(f"DOB filled: {dob}")

        self.select_relationship()
        self.click_save()
        self.logger.info("Dependent saved")

    def edit_dependent(self, edit_name):
        # Edit first dependent row.
        self.logger.info(f"Editing dependent to: {edit_name}")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Child One", exact=True))
        row.locator("i.bi-pencil-fill").click()
        name_field = self.name_input_field
        name_field.clear()
        name_field.first.fill(edit_name)
        self.click_save()

    def delete_dependent(self):
        # Delete first dependent.
        self.logger.info("Deleting dependent")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("Child One", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.confirm_delete()


    #  Immigration 

    def select_issued_by(self):
        # Click on dropdown
        self.issued_by_dropdown.click()
        # Select India
        self.dropdown_options.filter(has_text="India").first.click()

    def add_immigration(self, number, issued_date, expiry_date, eligible_status):
        # Add immigration document with number, dates, and eligible status
        self.logger.info(f"Adding immigration: {number}")
        self.immigration_add_button.first.click()
        self.logger.info("Immigration Add button clicked")
        number_field = self.number_input_field
        expect(number_field).to_be_visible()
        number_field.fill(number)
        self.logger.info(f"Immigration number filled: {number}")
        self.issue_date_input_field.fill(issued_date)
        self.logger.info(f"Issued date filled: {issued_date}")
        self.expiry_date_input_field.fill(expiry_date)
        self.logger.info(f"Expiry date filled: {expiry_date}")
        self.eligible_status_input_field.fill(eligible_status)
        self.logger.info(f"Eligible status filled: {eligible_status}")
        self.select_issued_by()
        self.click_save()
        self.logger.info("Immigration document saved")

    def edit_immigration(self, edit_number):
        # Edit first immigration row.
        self.logger.info(f"Editing immigration to: {edit_number}")
        self.logger.info(f"Editing first dependent to: {edit_number}")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("PASS123456", exact=True))
        row.locator("i.bi-pencil-fill").click()
        number_field = self.number_input_field
        expect(number_field).to_be_visible()
        number_field.fill(edit_number)
        self.click_save()

    def delete_immigration(self):
        # Delete first immigration record.
        self.logger.info("Deleting immigration")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("PASS123456", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.confirm_delete()

    #  Job
    def is_job_section_visible(self):
        try:
            loc = self.job_heading.first
            expect(loc).to_be_visible()
            return True
        except Exception:
            return False

    #  Salary
    def is_salary_section_visible(self):
        try:
            loc = self.salary_heading.first
            expect(loc).to_be_visible()
            return True
        except Exception:
            return False

    #  Report-to
    def is_report_to_section_visible(self):
        try:
            loc = self.report_to_heading.first
            expect(loc).to_be_visible()
            return True
        except Exception:
            return False

    #  Qualifications: Work Experience

    def add_work_experience(self, company, job_title, from_date, to_date):
        # Add work experience with company, job title, and dates
        self.logger.info(f"Adding work experience: {company}")
        self.work_experiance_add_button.first.click()
        self.logger.info("Work Experience Add button clicked")
        company_field = self.company_input_field
        expect(company_field).to_be_visible()
        company_field.fill(company)
        self.logger.info(f"Company filled: {company}")
        self.job_title_input_field.fill(job_title)
        self.logger.info(f"Job title filled: {job_title}")
        self.from_input_field.fill(from_date)
        self.logger.info(f"From date filled: {from_date}")
        self.to_input_field.fill(to_date)
        self.logger.info(f"To date filled: {to_date}")
        self.click_save()
        self.logger.info("Work experience saved")

    def edit_work_experiance(self, name):
        # Edit first work experience row.
        self.logger.info(f"Editing first work experience: {name}")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text(name, exact=True))
        row.locator("i.bi-pencil-fill").click()
        company_field = self.company_input_field
        expect(company_field).to_be_visible()
        company_field.fill(name)
        self.click_save()

    def delete_reusable_function(self,name):
        # Delete first work experience.
        self.logger.info("Deleting first work experience")
        self.logger.info("Deleting first dependent")
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text(name, exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.confirm_delete()

    #  Qualifications: Education 

    def select_education_level(self):
        # Click on dropdown
        self.level_dropdown.click()
        # Select Degree
        self.dropdown_options.filter(has_text="Bachelor's Degree").first.click()

    def add_education(self, institute ,year):
        # Add education record with institute and year
        self.logger.info(f"Adding education: {institute}")
        self.education_add_button.first.click()
        self.logger.info("Education Add button clicked")
        self.page.wait_for_timeout(500)
        self.select_education_level()
        self.logger.info("Education level selected")
        self.institute_input_field.fill(institute)
        self.logger.info(f"Institute filled: {institute}")
        self.year_input_field.fill(year)
        self.logger.info(f"Year filled: {year}")
        self.click_save()
        self.logger.info("Education saved")

    def edit_education(self, name):
        # Edit
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text(name, exact=True))
        row.locator("i.bi-pencil-fill").click()
        company_field = self.year_input_field
        expect(company_field).to_be_visible()
        company_field.fill(name)
        self.click_save()


    #  Qualifications: Skills 

    def select_skills(self):
        # Click on dropdown
        self.skills_dropdown.click()
        # Select Python
        self.dropdown_options.filter(has_text="Python").first.click()

    def add_skill(self, years_exp):
        # Add skill with years of experience
        self.logger.info(f"Adding skill with {years_exp} years experience")
        self.skills_add_button.first.click()
        self.logger.info("Skill Add button clicked")
        self.page.wait_for_timeout(500)
        self.select_skills()
        self.logger.info("Skill type selected")
        self.year_experiance_input_field.fill(years_exp)
        self.logger.info(f"Years of experience filled: {years_exp}")
        self.click_save()
        self.logger.info("Skill saved")

    def edit_skill(self, name):
        # Edit
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("Python", exact=True))
        row.locator("i.bi-pencil-fill").click()
        company_field = self.year_experiance_input_field
        expect(company_field).to_be_visible()
        company_field.fill(name)
        self.click_save()

    #  Qualifications: language 

    def select_language(self):
        # Click dropdown
        self.language_dropdown.click()
        # Select English
        self.dropdown_options.filter(has_text="English").first.click()

    def select_fluency(self):
        # Click on dropdown
        self.fluency_dropdown.click()
        # Select Reading
        self.dropdown_options.filter(has_text="Reading").first.click()

    def select_competency(self):
        self.competency_dropdown.click()
        self.dropdown_options.filter(has_text="Good").first.click()

    def add_language(self):
        # Add language with fluency and competency
        self.logger.info("Adding language")
        self.languages_add_button.first.click()
        self.logger.info("Language Add button clicked")
        self.select_language()
        self.logger.info("Language selected")
        self.select_fluency()
        self.logger.info("Fluency level selected")
        self.select_competency()
        self.logger.info("Competency level selected")
        self.click_save()
        self.logger.info("Language saved")

    def delete_language(self):
        # Delete
        row = self.page.locator("div.oxd-table-card").filter(
            has=self.page.get_by_text("English", exact=True)
        )
        # Click Delete icon in that specific row
        row.locator("i.bi-trash").click()
        self.confirm_delete()

    #  Memberships

    def select_membership(self):
        self.membership_dropdown.click()
        self.dropdown_options.filter(has_text="British Computer Society (BCS)").first.click()

    def select_subscription_paid_by(self):
        self.subscription_paid_by_dropdown.click()
        self.dropdown_options.filter(has_text="Company").first.click()

    def add_membership(self, amount):
        # Add membership with amount
        self.logger.info(f"Adding membership with amount: {amount}")
        self.membership_add_button.first.click()
        self.logger.info("Membership Add button clicked")
        self.page.wait_for_timeout(500)
        self.select_membership()
        self.logger.info("Membership type selected")
        self.select_subscription_paid_by()
        self.logger.info("Subscription paid by selected")
        self.amount_input_field.fill(amount)
        self.logger.info(f"Subscription amount filled: {amount}")
        self.click_save()
        self.logger.info("Membership saved")


    def edit_membership(self):
        # Edit first membership (amount and renewal date).
        self.logger.info("Editing first membership")
        row = self.page.locator("div.oxd-table-card").filter(has=self.page.get_by_text("British Computer Society (BCS)", exact=True))
        row.locator("i.bi-pencil-fill").click()
        amount_field = self.amount_input_field
        expect(amount_field).to_be_visible()
        amount_field.click()
        self.click_save()

    #  Attachments 


    def upload_attachment(self, file_path: str, comment: str):
        # Upload attachment with comment.
        self.logger.info("Uploading attachment")
        self.add_attachment()
        self.page.wait_for_timeout(500)
        self.page.locator("input[type='file']").set_input_files(file_path)
        self.page.get_by_placeholder("Type comment here").first.fill(comment)
        self.click_save()

    def delete_attachment_first(self):
        # Delete first attachment.
        self.logger.info("Deleting first attachment")
        self.click_delete_button()
        self.page.wait_for_timeout(300)
        self.confirm_delete()
