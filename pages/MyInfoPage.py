from playwright.sync_api import Page


class MyInfoPage:

    def __init__(self, page: Page):
        self.page = page

    # ---------- LOCATORS ----------
    my_info_menu = "a[href*='viewMyDetails']"
    save_btn = "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]"
    add_btn = "button:has-text('Add')"
    delete_icon = "i.bi-trash"
    confirm_delete = "button:has-text('Yes, Delete')"

    # ---------- NAVIGATION ----------
    def open_my_info(self):
        self.page.click(self.my_info_menu)

    def open_contact_details(self):
        self.page.get_by_role("link", name="Contact Details").click()

    def open_emergency_contacts(self):
        self.page.get_by_role("link", name="Emergency Contacts").click()

    def open_dependents(self):
        self.page.get_by_role("link", name="Dependents").click()

    def open_tab(self, name):
        self.page.get_by_role("link", name=name).click()

    # ---------- PERSONAL DETAILS ----------
    def update_first_name(self, name):
        self.page.get_by_placeholder("First Name").fill(name)
        self.page.locator(self.save_btn).first.click()

    def update_last_name(self, name):
        self.page.get_by_placeholder("Last Name").fill(name)
        self.page.locator(self.save_btn).first.click()

    def update_nickname(self, nickname):
        self.page.get_by_placeholder("Nickname").fill(nickname)
        self.page.locator(self.save_btn).first.click()

    def update_personal(self, first, middle, last):
        self.page.get_by_placeholder("First Name").click()
        self.page.get_by_placeholder("First Name").clear()
        self.page.get_by_placeholder("First Name").fill(first)
        self.page.get_by_placeholder("Middle Name").click()
        self.page.get_by_placeholder("Middle Name").clear()
        self.page.get_by_placeholder("Middle Name").fill(middle)
        self.page.get_by_placeholder("Last Name").click()
        self.page.get_by_placeholder("Last Name").clear()
        self.page.get_by_placeholder("Last Name").fill(last)

        self.page.locator(self.save_btn).click()

    def get_employee_id(self):
        return self.page.locator("input[name='employeeId']")

    # ---------- CONTACT DETAILS ----------

    def update_mobile(self, number):
        self.page.get_by_placeholder("Mobile").fill(number)
        self.page.locator(self.save_btn).first.click()

    def update_email(self, email):
        self.page.get_by_placeholder("Work Email").fill(email)
        self.page.locator(self.save_btn).first.click()

    def update_address(self, address):
        self.page.get_by_placeholder("Street 1").fill(address)
        self.page.locator(self.save_btn).first.click()

    def update_contact(self, mobile, email, address=None):
        self.page.get_by_placeholder("Mobile").fill(mobile)
        self.page.get_by_placeholder("Work Email").fill(email)
        if address:
            self.page.get_by_placeholder("Street 1").fill(address)
        self.page.locator(self.save_btn).first.click()

    # ---------- EMERGENCY CONTACTS ----------
    def add_emergency_contact(self, name, relation, mobile):
        self.page.click(self.add_btn)
        self.page.get_by_placeholder("Name").fill(name)
        self.page.get_by_placeholder("Relationship").fill(relation)
        self.page.get_by_placeholder("Mobile").fill(mobile)
        self.page.locator(self.save_btn).click()

    def delete_emergency_contact(self):
        self.page.locator(self.delete_icon).first.click()
        self.page.click(self.confirm_delete)

    # ---------- DEPENDENTS ----------
    def add_dependent(self, name, dob):
        self.page.click(self.add_btn)
        self.page.get_by_placeholder("Name").fill(name)
        self.page.get_by_role("combobox").select_option("Other")
        self.page.get_by_placeholder("Date of Birth").fill(dob)
        self.page.locator(self.save_btn).click()

    def delete_dependent(self):
        self.page.locator(self.delete_icon).first.click()
        self.page.click(self.confirm_delete)

    # ---------- ATTACHMENTS ----------
    def upload_attachment(self, file_path, comment):
        self.page.click(self.add_btn)
        self.page.set_input_files("input[type='file']", file_path)
        self.page.get_by_placeholder("Type comment here").fill(comment)
        self.page.locator(self.save_btn).click()
